from flask import Flask,jsonify,make_response,request,render_template,Response,current_app
from werkzeug import secure_filename
import os
app = Flask(__name__)

from model import User


UPLOAD_FOLDER = '/home/mugz/Projects/Rafiki/static'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/index')
def rafiki():
	return Response(render_template('index.html'))


@app.route('/register',methods=['GET', 'POST'])
def add_rafiki():

    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
        photo=filename

        name = request.form['name']
        email=request.form['email']
        password=request.form['pword']


        User().save_users(name,email,password,photo)
        return Response(render_template('login.html'))

    else:
         return Response(render_template('register.html'))

@app.route('/login',methods=['GET', 'POST'])
def auth():

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['pword']

        user = User().login(email,password)

        if user:
            return Response(render_template('index.html',photo=user['photo']))

    else:
        return Response(render_template('login.html'))

if __name__ == '__main__':
	app.run()
