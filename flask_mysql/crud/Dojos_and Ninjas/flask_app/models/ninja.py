from dataclasses import dataclass
from winreg import QueryInfoKey
from flask_app.config.mysqlconnection import connectToMySQL


class Ninja:
    DB="dojos_and_ninjas_schema"
    def __init__(self, db_data):
        self.id=db_data['id']
        # only need for a hidden form on edit-ninja.html
        self.dojo_id=db_data['dojo_id']
        self.first_name=db_data['first_name']
        self.last_name=db_data['last_name']
        self.age=db_data['age']
        self.created_at=db_data['created_at']
        self.updated_at=db_data['updated_at']

    @classmethod
    def create_ninja(cls,data):
        query="""
            INSERT INTO ninjas (dojo_id, first_name, last_name, age)
            VALUES (%(dojo_id)s,%(first_name)s,%(last_name)s,%(age)s);
            """
        result=connectToMySQL(cls.DB).query_db(query,data)
        print("__CREATE_NINJA__", result)
        return result    

    @classmethod
    def delete_ninja(cls,id):
        data={"id":id}
        query="DELETE FROM ninjas WHERE id=%(id)s;"
        result=connectToMySQL(cls.DB).query_db(query,data)
        print("__DELETE USER__",result)
        return result

    @classmethod
    def get_ninja(cls,id):
        data= {"id":id}
        query = "SELECT * FROM ninjas WHERE id=%(id)s;"
        results=connectToMySQL(cls.DB).query_db(query,data)
        print("_GET ONE NINJA  BY ID_", results)
        return cls(results[0])


    @classmethod
    def update_ninja(cls,data):
        # data={"id":id}
        query = "UPDATE ninjas SET first_name=%(first_name)s,last_name=%(last_name)s, age=%(age)s WHERE id=%(id)s;"
        result=connectToMySQL(cls.DB).query_db(query,data)
        print("__UPDATE NINJA__", result)
        return result