from flask import Flask,jsonify,make_response,request,render_template,Response,current_app,flash
from werkzeug import secure_filename
import os

from model import User

app = Flask(__name__)
app.secret_key ="371a7a78d634dd71ce5f215d4827ea919d00ea50a9e20482d7adefd8a5156b78"


UPLOAD_FOLDER = '/home/mugz/Projects/Rafiki/static'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/index')
def rafiki():
	return Response(render_template('index.html'))

@app.route('/about')
def about():
    return Response(render_template('about.html'))



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
        flash('Registration Sucessful')
        return Response(render_template('index.html'))


@app.route('/login',methods=['GET', 'POST'])
def auth():

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['pword']

        user = User().login(email,password)

        if user:
            flash('Login Succesful')
            return Response(render_template('index.html'))

        else:
            flash('Login Failure')
            return Response(render_template('index.html'))

if __name__ == '__main__':

    app.run()
