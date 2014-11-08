from flask import Flask,render_template

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/name/<name>')
def monthly(name):
    return render_template("index.html",header=name)

@app.route('/name')
def blank():
    name = "Hallo SPASST"
    return render_template("index.html",header=name)



@app.route('/link')
def link():
    return "DU HURENSOHN"