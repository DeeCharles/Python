from flask import Flask, render_template
app = Flask(__name__)
# our index route will handle rendering our form
# @app.route('/')
# def checker():
#     return render_template("indexu.html")

@app.route('/')
def render_boxes():
    return render_template("checker.html",num = 8)

@app.route('/row/<int:num2>')
def render_boxes2(num2):
    return render_template("checker.html", num=8,num2=num2)

@app.route('/row/column/<int:num>/<int:num2>')
def render_boxes3(num,num2):
    return render_template("checker.html",num=num,num2=num2)

@app.route('/row/column/color/<int:num>/<int:num2>/<color1>/<color2>')
def render_boxes4(num,num2,color1,color2):
    return render_template("checker.html",num=num,num2=num2,color1=color1,color2=color2)

if __name__=="__main__":
    app.run(debug=True)
    