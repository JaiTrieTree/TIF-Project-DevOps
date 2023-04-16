from . import db

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    instructor = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)

