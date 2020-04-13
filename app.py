from flask import Flask, render_template, url_for,redirect, request
from flask_bootstrap import Bootstrap
from flask_mysqldb  import MySQL
import yaml
import bios

# db = bios.read('db.yaml')

app = Flask(__name__)
db = yaml.load(open('db.yaml'),Loader=yaml.FullLoader)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER']= 'newuser'
app.config['MYSQL_PASSWORD']= 'Newuser123'
app.config['MYSQL_DB'] = 'my_database'

mysql = MySQL(app)
bootstrap = Bootstrap(app)
fruits = ['Apple', 'Mango', 'Grapes', 'Pineapple']

@app.route('/', methods=['GET','POST'])
def index():        
   if request.method == "POST":
    
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/abaut')
def abaut():
    return redirect(url_for('about'))

if __name__ == '__main__':
    app.run(debug=True)