from flask import render_template, redirect, session, request

# line below is to invoke class methods
from flask_app.models import user

from flask_app import app

# import the class from user.py
# from user import User

@app.route('/') 
def index():
    users = user.User.get_all_users()
    print(users)
    return render_template("read.html", all_users = users)

@app.route('/new/users')
def new_user():
    return render_template("create.html")

@app.route("/add/user", methods=["POST"])
def add_user():
    print("Hello", request.form)
    # saves to db and returns new user id
    user_id=user.User.create_user(request.form)
    return redirect(f"/users/{user_id}")

@app.route("/users/<int:id>")
def get_user(id):
    one_user=user.User.get_user_by_id(id)
    return render_template ("read_one.html", one_user=one_user)

@app.route('/users/<int:id>/edit')
def edit_user(id):
    # print(Name.request.form["id"])- don't need, used hidden key
    # user.User.edit_user(id)
    # This is the get for user by id
    # below variable is assigned to model .py file.class.class_method
    this_user=user.User.get_user_by_id(id)
    return render_template ("edit.html",this_user=this_user)

@app.route('/users/<int:user_id>/update_user', methods=["POST"])
def update_user(user_id):
    # Update returns none
    user.User.edit_user(request.form)
    return redirect(f"/users/{user_id}")
    

@app.route("/delete/user/<int:id>")
def delete_user(id):
    user.User.delete_user(id)
    return redirect("/")

