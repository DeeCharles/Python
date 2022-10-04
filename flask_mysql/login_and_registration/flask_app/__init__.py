from flask import Flask

app = Flask(__name__)
# secret key is needed for sessions
app.secret_key = 'ca2a5b4b0c0b452bbdbe538dd0be80ac'
