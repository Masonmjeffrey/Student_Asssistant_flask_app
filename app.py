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


@app.route('/concat_nums/<nnum1>/<nnum2>/')
def concat_nums(nnum1, nnum2):
    concated_nums = str(nnum1)+str(nnum)
    return str(concated_nums)
