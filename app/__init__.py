from flask import Flask
import mysql.connector

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'teluguitfactory'
app.config['MYSQL_PASSWORD'] = 'teluguitfactory'
app.config['MYSQL_DB'] = 'teluguitfactorydb'

mysql = mysql.connector.connect(
    host=app.config['MYSQL_HOST'],
    user=app.config['MYSQL_USER'],
    password=app.config['MYSQL_PASSWORD'],
    database=app.config['MYSQL_DB']
)

from app import course, login, cart, price_list

