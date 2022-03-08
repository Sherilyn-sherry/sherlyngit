from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Good Mornig Everyone</h1>"

@app.route("/greeting/<user>")
def greeting(user):
    return render_template("greeting.html",name = user)

@app.route("/index")
def index():
    return render_template("index.html")

@app.route('/evaluation/<int:score>')

def evaluation(score):
    return render_template('evaluation.html', marks = score)

@app.route("/about-us")
def about():
    return render_template("about-us.html")

    
if __name__ == '__main__':
    app.run(debug=True)
