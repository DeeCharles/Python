
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'smilejly' # set a secret key for security purposes

# Counts the number of times the root route ('/') has been viewed
@app.route('/')
def counter():
    if "count" not in session:
        # Session uses keys, therefore use []. This set key to value "0"
        session["count"]=1
        print("key 'count' does Not exist")
    else:
        session["count"]+=1     
        print("key exists")
    return render_template('index.html')  

@app.route('/destroy_session')
def destroy_session():
    # Clears ALL keys.  Use
    session.clear()
    # session.pop('key_name')clears specific key if there is more than one
    # line below causes ('/') on line 9 to start counting again
    return redirect("/") 

# NINJA BONUS: Add a +2 button underneath the counter and a new route that will increment the counter by 2
@app.route('/increment')
def counter_two():
    if "count" in session:
        session["count"]+=1
    else:
        session["count"]=1
    return redirect('/')

# NINJA BONUS: Add a Reset button to reset the counter.  Same as destroy_session above, except with a button
@app.route('/reset',methods=['POST'])
def counter_reset():
    session.clear()
    return redirect('/')

# SENSEI BONUS: Add a form that allows the user to specify the increment of the counter and have the counter increment accordingly
@app.route('/form/<increment>', methods=['POST'])    
def form():
    pass




# @app.route('/users', methods=['POST'])
# def create_user():
#     print("Got Post Info")
#     # Here we add two properties to session to store the name and email
#     session['username'] = request.form['name']
#     session['useremail'] = request.form['email']
#     return redirect('/show')

# @app.route('/show')
# def show_user():
#     return render_template('index.html', name_on_template=session['username'], email_on_template=session['useremail'])

if __name__ == "__main__":
    app.run(debug=True)
