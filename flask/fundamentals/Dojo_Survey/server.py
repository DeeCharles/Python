from cgitb import html
from flask import Flask, render_template, session, redirect, request
app = Flask(__name__)

app = Flask(__name__)
app.secret_key = 'smilejly'

# process route will show info from form
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    print("Got Post Info")
    print(request.form['name'])
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    return redirect("/result")

@app.route('/result')
def result():
    return render_template("/result.html")

# @app.route('/show', methods=['POST'])
# def show():
#     print("Got Post Info")
#     # Here we add two properties to session to store the name and email
#     session['name'] = request.form['name']
#     session['location'] = request.form['location']
#     return redirect('/process')




if __name__ == "__main__":
    app.run(debug=True)



