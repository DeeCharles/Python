from flask_app.models import ninja
from flask_app.config.mysqlconnection import connectToMySQL



class Dojo:
    DB="dojos_and_ninjas_schema"
    def __init__(self, db_data):
        self.id=db_data['id']
        self.name=db_data['name']
        self.created_at=db_data['created_at']
        self.updated_at=db_data['updated_at']
        # Create a list to add all ninjas associated with Dojo
        self.ninjas=[]

# Query your database

    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(cls.DB).query_db(query)
        print("_ALL DOJOS_", results)
        # Create an empty list to append our instances of dojos
        dojos = []
        # Iterate over the db results and create instances of dojos with cls.
        for row in results:
            dojos.append( cls(row) )
        return dojos

    @classmethod
    def create_dojo(cls,data):
        query="INSERT INTO dojos (name) VALUES (%(name)s);"
        result=connectToMySQL(cls.DB).query_db(query,data)
        print("__CREATE_USER__", result)
        return result
        
    @classmethod
    def get_dojo_by_id(cls, id):
        data= {"id":id}
        query = "SELECT * FROM dojos WHERE id=%(id)s;"
        results=connectToMySQL(cls.DB).query_db(query,data)
        print("_GET ONE USER BY ID_", results)
        return cls(results[0])


# still have questions about this
    @classmethod
    def get_dojo_with_ninja(cls,id):
        data={"id":id}
        query = """
        SELECT * 
        FROM dojos 
        LEFT JOIN ninjas 
        ON ninjas.dojo_id=dojos.id 
        WHERE dojos.id=%(id)s
        ;"""
        results=connectToMySQL(cls.DB).query_db(query,data)
        print("__RESULTS__", results)
        dojo=cls(results[0])
        for row_from_db in results:
            # Prevents populating table with None
            if row_from_db["ninjas.id"]== None:
                return dojo
            # must have all columns
            ninja_data={
                # only need table name for id, in this case table name is ninjas
                "id":row_from_db["ninjas.id"],
                # added due to adding back into constructor
                "dojo_id":row_from_db["dojo_id"],
                "first_name":row_from_db["first_name"],
                "last_name":row_from_db["last_name"],
                "age":row_from_db["age"],
                "created_at":row_from_db['created_at'],
                "updated_at":row_from_db['updated_at']
                }
                # dojo below is from dojo above and  is ninja.Ninja = model.class(argument) 
            dojo.ninjas.append(ninja.Ninja(ninja_data))
            print("dojo", dojo)
        # why returning this dojo- returns with new results
        return dojo