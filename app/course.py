from flask import render_template
from app import app

@app.route('/courses')
def course_page():
    # Fetch courses from the database
    courses = [
        {"title": "Course 1", "description": "Course 1 description", "instructor": "John Doe"},
        {"title": "Course 2", "description": "Course 2 description", "instructor": "Jane Doe"},
        {"title": "Course 2", "description": "Course 2 description", "instructor": "Jane Doe"},
    ]

    return render_template('course_page.html', courses=courses)

