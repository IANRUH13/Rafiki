from flask import Flask,jsonify,make_response,request,render_template,Response,current_app,flash,redirect,url_for
from werkzeug import secure_filename
from flask_jwt_extended import (
JWTManager, jwt_required, create_access_token,
get_jwt_identity,set_access_cookies,unset_jwt_cookies,jwt_optional
)
import os


from model import User

app = Flask(__name__)
app.secret_key ="371a7a78d634dd71ce5f215d4827ea919d00ea50a9e20482d7adefd8a5156b78"


UPLOAD_FOLDER = '/home/mugz/Projects/Rafiki/static'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

jwt = JWTManager(app)
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
app.config['JWT_COOKIE_CSRF_PROTECT'] = False



def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/index')
@jwt_optional
def rafiki():
    current_user = get_jwt_identity()
    if current_user:
        photo = current_user[2]
        return Response(render_template('index.html',photo=photo))

    return Response(render_template('index.html'))



@app.route('/about',methods=['GET'])
@jwt_optional
def about():
    current_user = get_jwt_identity()
    if current_user:
        photo = current_user[2]
        return Response(render_template('about.html',photo=photo))


    return Response(render_template('about.html'))



@app.route('/share',methods=['GET','POST'])
@jwt_optional
def share():
    current_user = get_jwt_identity()
    if request.method == 'POST':
        if current_user:
            photo = current_user[2]
            email = current_user[1]
            story = request.form['story']
            User().share(email,story)

            stories =  User().stories()
            return Response(render_template('share.html',photo=photo,stories= stories))

        else:
            email = "jdoe@email.com"
            story = request.form['story']
            User().share(email,story)


    if current_user:
        photo = current_user[2]
        stories =  User().stories()
        return Response(render_template('share.html',photo=photo,stories= stories))


    else:
        stories =  User().stories()
        return Response(render_template('share.html',stories= stories))



@app.route('/search',methods=['GET','POST'])
def find():
    search = request.form['story']
    found = User().search_post(search)

    val = 0
    for item in found:
        val += 1

    if found:
        return Response(render_template('search.html', stories=found, count=val))
    else:
        return Response(render_template('search.html', stories=found, count="Not"))



@app.route('/respond/<int:share_id>',methods=['GET','POST'])
@jwt_optional
def respond(share_id):
    current_user = get_jwt_identity()

    if request.method == 'POST':
        if current_user:
            photo = current_user[2]
            email = current_user[1]
            comment = request.form['story']
            User().respond(share_id, comment, email)
            return redirect(url_for('respond',share_id=share_id))

        else:
            email = "jdoe@email.com"
            comment = request.form['story']
            User().respond(share_id, comment, email)
            return redirect(url_for('respond',share_id=share_id))


    if current_user:
        photo = current_user[2]
        resp = User().get_respond(share_id)
        headin = User().get_title(share_id)
        title = headin[0]
        posted_on = headin[1]
        return Response(render_template('respond.html',photo=photo,stories=resp,title=title,posted_on=posted_on))


    else:
        resp = User().get_respond(share_id)
        headin = User().get_title(share_id)
        title = headin[0]
        posted_on = headin[1]

        return Response(render_template('respond.html',stories=resp,title=title,posted_on=posted_on))


@app.route('/register',methods=['POST'])
def add_rafiki():

    file = request.files['file']
    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
        photo=filename
    else:
        photo = 'user.png'

    name = request.form['name']
    email=request.form['email']
    password=request.form['pword']
    User().save_users(name,email,password,photo)
    user = User().login(email,password)
    access_token = create_access_token(identity=user, expires_delta=False)
    # Set the JWT cookies in the response
    resp = make_response(redirect(url_for('rafiki')))
    set_access_cookies(resp, access_token)
    flash("Success")
    return resp

    return Response(render_template('index.html'))



@app.route('/logout',methods=['GET','POST'])
def logout():
    resp = make_response(redirect(url_for('rafiki')))
    unset_jwt_cookies(resp)
    flash("Success")
    return resp


@app.route('/login',methods=['POST'])
def auth():
    email = request.form['email']
    password = request.form['pword']

    user = User().login(email,password)

    if user:
        access_token = create_access_token(identity=user, expires_delta=False)
        # Set the JWT cookies in the response
        resp = make_response(redirect(url_for('rafiki')))
        set_access_cookies(resp, access_token)
        flash("Success")
        return resp

    else:
        flash('Error')
        return Response(render_template('index.html'))


if __name__ == '__main__':

    app.run()
