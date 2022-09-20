# from flask import Flask, render_template  # added render_template!
# app = Flask(__name__)
# @app.route('/play')
# def index(): # Instead of returning a string,return the result of the render_template method, passing in the name the HTML file
#     return render_template("index.html")

#     # return render_template("index.html", phrase="hello", times=5)	# notice the 2 new named arguments!
    
# if __name__=="__main__":
#     app.run(debug=True)

from flask import Flask, render_template  # added render_template!
app = Flask(__name__) 
@app.route('/play/<color>/<int:num>')
def index(num): # Instead of returning a string,return the result of the render_template method, passing in the name the HTML file
    return render_template("index.html", times=int(num))

from flask import Flask, render_template  # added render_template!
app = Flask(__name__) 
@app.route('/play/<color>/<int:num>')
def index(color,num): # Instead of returning a string,return the result of the render_template method, passing in the name the HTML file
    return render_template("index.html", color=color,times=int(num))

    # return render_template("index.html", int(x))	# notice the named argument!
    
if __name__=="__main__":
    app.run(debug=True)
    


    

