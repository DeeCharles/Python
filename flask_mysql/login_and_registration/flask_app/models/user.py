from flask_app.config.mysqlconnection import connectToMySQL

# These imports are for login registration.

import bcrypt
from flask_app import app
from flask import flash, session
from flask_bcrypt import Bcrypt
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
# use flash when validations fail

bcrypt = Bcrypt(app)

class User:
    DB="log_reg_users"

    def __init__(self,data):
        self.id=data["id"]
        self.first_name=data["first_name"]
        self.last_name=data["last_name"]
        self.email=data["email"]
        self.password=data["password"]
        self.created_at=data["created_at"]
        self.updated_at=data["updated_at"]

    # CREATE user SQL

    @classmethod
    def register(cls,user_data):
        # have to create new dictionary since password is hashed and request.form dictionary is immutable - will get tuple error.  This can be done here or in the controller
        if not cls.validate_register(user_data):
            return False
        data = {
            "first_name":user_data["first_name"],
            "last_name":user_data["last_name"],
            # "email":user_data["email"].lower(),
            "email":user_data["email"],
            "password":bcrypt.generate_password_hash(user_data["password"])
        }
        print("USER DATA", user_data["password"],data["password"])
        # if you use user_data.password, you will get Attribute error:'ImmutableMultiDict' object has no attribute 'password'
        
        query = """
        INSERT INTO users(first_name,last_name,email,password)
            VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s);
        """
        # INSERT will always return id which is what the result is
        id=connectToMySQL(cls.DB).query_db(query,data)
        print("__INSERT USER ID__", id)
        return id
        # lines below may replace line 51 and 52
        # session['user_id'] = id
        # session['user_name'] = f"{data['first_name']} {data['last_name']}"
        # return True


    # READ user SQL
        
    @classmethod
    def get_user_by_email(cls,email):
        data = {"email":email}
        query = """
        SELECT * FROM users
        WHERE email = %(email)s;
        """
        result = connectToMySQL(cls.DB).query_db(query,data)
        if len(result) == 0:
            return False
        else:
            return cls(result[0])

    # UPDATE user SQL

    # DELETE user SQL

    # Login Registration SQL
        
    @staticmethod
    # user is parameter being passed from the form in session
    def validate_register(user):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        is_valid = True
        if len(user['first_name']) < 2:
            is_valid = False
            flash('Your first name needs to be at least two characters long.') 
        if len(user['last_name']) < 2:
            is_valid = False
            flash('Your last name needs to be at least two characters long.') 
        if len(user['password']) < 8:
            is_valid = False
            flash('Your password needs to be at least eight characters long.') 
        if not EMAIL_REGEX.match(user['email']):
            flash('Please use a valid email address.')
            is_valid = False
        if User.get_user_by_email(user['email']):
        # if User.get_user_by_email(user['email'].lower()):
            flash('This email is in use.')
            is_valid = False
        if user['password'] != user['confirm_password']:
            flash("Your passwords don't match")
            is_valid = False
        return is_valid

    @staticmethod
    def login_user(data):
        this_user = User.get_user_by_email(data['email'])
        if this_user:
            if bcrypt.check_password_hash(this_user.password, data['password']):
                session['user_id'] = this_user.id
                # We have to do below b/c it is a string and not integer???
                session['user_name'] = f"{this_user.first_name} {this_user.last_name}"
                return True
        flash('Your login failed!')
        return False
