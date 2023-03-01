from flask import Flask
import psycopg2


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/dbtest')
def index():
    conn = psycopg2.connect("postgres://sample_flask_db_user:7qN9gGyh8FcUmg99oDG8tdv4QHelRJMm@dpg-cfvrsul269v0ptnleuhg-a/sample_flask_db")
    return "it works"