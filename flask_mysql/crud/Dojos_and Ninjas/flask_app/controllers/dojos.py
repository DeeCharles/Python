
from flask_app import app
from flask import render_template, redirect, request
from flask_app.models import dojo

@app.route('/dojos')
def display():
    # line below is assigned to model.py file.class.class_method
    all_dojos=dojo.Dojo.get_all_dojos()
    print("__ALL DOJOS__", all_dojos)
    return render_template("dojos.html", all_dojos=all_dojos)

@app.route('/add/dojo', methods=["POST"])
def add_dojo():
    print("__ADD DOJO__"),(request.form)
    dojo.Dojo.create_dojo(request.form)
    # can't render_template on a POST
    return redirect ("/dojos")

@app.route("/dojos/<int:id>")
def get_dojo(id):
    one_dojo=dojo.Dojo.get_dojo_with_ninja(id)
    print(one_dojo)
    return render_template("dojo-show.html", one_dojo=one_dojo)



