from flask import Flask
from marksupsafe import escape
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/capitalize/<word>/')
def capitalize(word):
    return word.capitalize()
