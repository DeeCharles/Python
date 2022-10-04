from flask_app import app
from flask import render_template,redirect,request,session
from flask_app.models import user

# CREATE USERS

@app.route("/register", methods=['POST'])
def register():
    # if not user.User.validate_register(request.form):
    # return redirect("/")
    # user_id=user.User.register(request.form)
    # return redirect("/")
    if user.User.register(request.form):
        print('USER ID is user_id')
        return redirect('/users/profile')
    return redirect('/')


# READ USERS

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/users/profile')
def profile():
    if not 'user_id' in session:
        return redirect('/')
    return render_template('profile.html')

# logout route

@app.route('/users/logout')
def logout_user():
    session.clear()
    return redirect('/')

# login route

@app.route("/users/login", methods = ['POST'])
def login_user():
    if user.User.login_user(request.form):
        return redirect('/users/profile')
    return redirect('/')