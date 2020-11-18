from sqlalchemy import Column, Integer, String, DateTime, Boolean, Unicode, Text
from sqlalchemy.orm import relationship
from budget import app, db

# The users table stores all of the budget applications users
class User(db.Model):
    """
    Represents a Budget app user.
    """
    __tablename__ = 'users'

    # Basic user info
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50), nullable=False)
    middle_name = db.Column(db.String(50), nullable=True)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False, index=True)
    username = db.Column(db.String(120), unique=True, nullable=False, index=True)
    password = db.Column(db.String(255), nullable=False)
    
    # Tracking information
    last_login = Column(DateTime())
    last_updated = Column(DateTime())

    # Relationships 

    def __init__(self, first_name, last_name, email, username, password, middle_name=None, last_login=None, last_updated=None):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.password = password
        self.last_login = last_login
        self.last_updated = last_updated

    def __str__(self):
        return '<User id=%s email=%s>' % (self.id, self.email)

    def create(self):
        db.session.add(self)
        db.session.commit()

        return self

