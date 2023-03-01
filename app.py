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

@app.route("/db_create_select")
def db2():
    conn = psycopg2.connect("postgres://sample_flask_db_user:7qN9gGyh8FcUmg99oDG8tdv4QHelRJMm@dpg-cfvrsul269v0ptnleuhg-a/sample_flask_db")
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Basketball (
        City varchar(255)
        LastName varchar(255)
        FirstName varchar(255)
        teamName varchar(255);
        )
    ''')
    conn.commit()
    cur.execute('''
        INSERT INTO Basketball (City, LastName, FirstName, TeamName)
        VALUES ('Boston', 'Tatum', 'Jayson', 'Celtics');
    ''')
    conn.commit()
    cur.execute('''
        SELECT * FROM Basketball;
    ''')
    records = cur.fetchall()
    conn.close()
    return records