from flask import render_template
from app import app

@app.route('/cart')
def cart():
    # Fetch courses from the database
    cart = [
        {"title": "Course 1", "description": "Course 1 description", "instructor": "John Doe"},
    ]

    return render_template('cart.html', cart=cart)

