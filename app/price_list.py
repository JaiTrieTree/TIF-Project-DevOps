from flask import render_template
from app import app

@app.route('/price_list')
def price_list():
    # Fetch courses and prices from the database
    courses = [
        {"title": "Course 1", "price": 49.99},
        {"title": "Course 2", "price": 59.99},
    ]

    return render_template('price_list.html', courses=courses)

