from flask import render_template, request, redirect, url_for
from app import app

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Authenticate and authorize user here
        return redirect(url_for('course_page'))
    return render_template('login.html')

