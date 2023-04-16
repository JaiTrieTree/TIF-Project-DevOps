#from flask import Flask
#import mysql.connector

#app = Flask(__name__)

#app.config['MYSQL_HOST'] = 'localhost'
#app.config['MYSQL_USER'] = 'root'
#app.config['MYSQL_PASSWORD'] = 'teluguitfactory'
#app.config['MYSQL_DB'] = 'teluguitfactorydb'

#mysql = mysql.connector.connect(
#    host=app.config['MYSQL_HOST'],
#    user=app.config['MYSQL_USER'],
#    password=app.config['MYSQL_PASSWORD'],
#    database=app.config['MYSQL_DB']
#)

#from app import course, login, cart, price_list
from flask import Flask
from flask_mysqldb import MySQL
from flask import session

app = Flask(__name__)

# Update these placeholders with your MySQL credentials and database name
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'teluguitfactory'
app.config['MYSQL_PASSWORD'] = 'teluguitfactory'
app.config['MYSQL_DB'] = 'teluguitfactorydb'

# Add a secret key for session support
app.secret_key = 'teluguitfactory'

mysql = MySQL(app)

from app import course, login, cart, price_list

# Redirect the root URL to the login page
@app.route('/')
def index():
    return redirect(url_for('login'))
