from flask import Flask
#The line above is bringing in the class Flask from flask on your PC

#This line instantiates flask
app = Flask(__name__)
app.secret_key = 'smilejly' # set a secret key for security purposes