from flask import Flask, render_template # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route('/dojo')          
def dojo():
    return 'Dojo'


@app.route('/say/<string:name>')
def say(name):
    print(name)
    return f"Hi,{name.capitalize()}!"

# localhost:5000/repeat/35/hello - have it say "hello" 35 times
# localhost:5000/repeat/80/bye - have it say "bye" 80 times
# localhost:5000/repeat/99/dogs - have it say "dogs" 99 times
# @app.route('/repeat/<int:num>/<string:word>')
@app.route('/repeat/<int:num>/<string:word>')
def repeat(num,word):
    return f'"{word}", {num} times'



# SENSEI BONUS: Ensure that if the user types in any route other than the ones specified, they receive an error message saying "Sorry! No response. Try again."

# from flask import render_template

# @app.errorhandler(404)
# def page_not_found(e):
#     # note that we set the 404 status explicitly
#     return render_template('404.html'), 404,  "Sorry! No response. Try again."

@app.errorhandler(404) 
def invalid_route(e): 
    print(e)
    return "Sorry! No response. Try again."


# app.run(debug=True) should be the very last statement! 

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.