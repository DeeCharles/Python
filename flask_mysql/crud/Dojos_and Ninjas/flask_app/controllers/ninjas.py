from flask_app import app
from flask import render_template, redirect, request
from flask_app.models import ninja, dojo

# @app.route('/dojos                /<dojo.id>')
# def display():
#     # line below is assigned to model.py file.class.class_method
#     all_ninjas=ninja.Ninja.get_all_ninjas()
#     print(all_ninjas)
#     return render_template("dojos.html", all_dojos=all_ninjas)

@app.route('/add/ninja', methods=['POST'])
# @app.route('/ninjas', methods=['POST'])
def add_ninja():
    print("__ADD NINJA__"),(request.form)
    ninja.Ninja.create_ninja(request.form)
    # can't render_template on a POST
    return redirect ("/dojos")

@app.route('/ninjas')
def new_ninja():
    all_dojos=dojo.Dojo.get_all_dojos()
    print("__NEW NINJA__")
    return render_template ("ninjas.html",all_dojos=all_dojos)

@app.route('/delete/<int:dojo_id>/ninja/<int:id>')
def delete_ninja(dojo_id,id):
    ninja.Ninja.delete_ninja(id)
    return redirect(f"/dojos/{dojo_id}")

@app.route('/ninjas/edit/<int:id>')
def update_ninja(id):
    return render_template("edit-ninja.html",this_ninja=ninja.Ninja.get_ninja(id))


@app.route('/edit/ninja/<int:id>', methods=['POST'])
def edit_ninja(id):
    # combined request.form with int:id above from url and therefore needed ninja_info dictionary
    ninja_info={"first_name":request.form['first_name'],
    "last_name":request.form['last_name'], 
    "age":request.form['age'],
    "id":id}
    print("__EDIT NINJA__"),(ninja_info)
    ninja.Ninja.update_ninja(ninja_info)
    # can't render_template on a POST
    # hidden value dojo_id came from edit-ninja.html
    return redirect (f"/dojos/{request.form['dojo_id']}")

