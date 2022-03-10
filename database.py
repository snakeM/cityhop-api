from main import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

class Passwords(db.Model):
    user_id = db.Column(db.String(320), db.ForeignKey('users.user_id'), primary_key=True)
    password = db.Column(db.String(100))

class Users(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(120), nullable=False)
    last_name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(320), unique=True, nullable=False)
    phone_number = db.Column(db.String(64), nullable=False)

class Locations(db.Model):
    location_id = db.Column(db.Integer, primary_key=True)
    location_name = db.Column(db.String(128))

class Scooters(db.Model):
    scooter_id = db.Column(db.Integer, primary_key=True)
    availability = db.Column(db.Integer)
    location_id = db.Column(db.Integer, db.ForeignKey('locations.location_id'))

class Trips(db.Model):
    hire_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    scooter_id = db.Column(db.Integer, db.ForeignKey('scooters.scooter_id'))
    start_time = db.Column(db.String(32))
    hire_length = db.Column(db.String(32))
    ongoing = db.Column(db.Integer)

class Feedback(db.Model): 
    feedback_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    date = db.Column(db.String(32), nullable=False)
    comment = db.Column(db.String(512), nullable=False)

class Cards(db.Model):
    card_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    card_num = db.Column(db.String(128), nullable=False)
    expiry = db.Column(db.String(128), nullable=False)
    cvv = db.Column(db.String(128), nullable=False)
    post_code = db.Column(db.String(128), nullable=False)


