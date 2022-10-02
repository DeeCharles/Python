# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the friend table from our database
class User:
    DB="users"
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    @classmethod
    def get_all_users(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(cls.DB).query_db(query)
        print("_ALL USERS_", results)
        # Create an empty list to append our instances of users
        users = []
        # Iterate over the db results and create instances of users with cls.
        for row in results:
            users.append( cls(row) )
        return users
                
    @classmethod
    def create_user(cls,data):
        query="INSERT INTO users (first_name,last_name, email) VALUES (%(first_name)s,%(last_name)s,%(email)s);"
        # variable below called result is the id for the user
        result=connectToMySQL(cls.DB).query_db(query,data)
        print("_CREATE USER_",result)
        return result

    @classmethod
    def delete_user(cls,id):
        data={"id":id}
        query="DELETE FROM users WHERE id=%(id)s;"
        result=connectToMySQL(cls.DB).query_db(query,data)
        print("_CREATE USER_",result)
        return result

    @classmethod
    def get_user_by_id(cls, id):
        data= {"id":id}
        query = "SELECT * FROM users WHERE id=%(id)s;"
        results=connectToMySQL(cls.DB).query_db(query,data)
        print("_GET ONE USER BY ID_", results)
        return cls(results[0])

    @classmethod
    # passing data directly from  edit.html form by using hidden input
    def edit_user(cls, data):
        # data={"id":id}
        query = "UPDATE users SET first_name=%(first_name)s,last_name=%(last_name)s, email=%(email)s WHERE id=%(id)s;"
        return connectToMySQL(cls.DB).query_db(query,data)
        
        

    
