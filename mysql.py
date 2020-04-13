from flask import Flask
from flask_mysqldb import MySQL
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER']= 'root'
app.config['MYSQL_PASSWORD']= 'root'
app.config['MYSQL_DB'] = 'my_database'

mysql = MySQL(app)

cur = mysql.connection.cursor()
cur.execute("SELECT * FROM USER")
fetchdata = cur.fetchall()
cur.close()
