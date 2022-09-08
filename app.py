from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
@app.route('/capitalize/<word>/')
def capitalize(word):
    return '<p>{}</p>'.format(escape(word.capitalize()))
