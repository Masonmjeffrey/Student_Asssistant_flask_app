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
    return str(n1+n2)


@app.route('/concat_nums/<n1>/<n2>/')
def concat_nums(n1, n2):
    return str(n1) + str(n2)
