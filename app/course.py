from flask import Blueprint, render_template
from app import mysql

course = Blueprint('course', __name__)

@course.route('/course', endpoint='course_page')
def course_page():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM courses")
    courses = cur.fetchall()
    cur.close()
    return render_template('course_page.html', courses=courses)

