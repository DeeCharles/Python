from flask_app import app
# line above come from __init__.py

from flask_app.controllers import dojos, ninjas


if __name__ == "__main__":
    app.run(debug=True)





