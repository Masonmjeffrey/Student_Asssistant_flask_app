from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/capitalize/<word>/')
def capitalize(word):
    return word.capitalize()


@app.route('/add/<int:n1>/<int:n2>/')
def add(n1, n2):
    sumnum = n1+n2
    return str(sumnum)
