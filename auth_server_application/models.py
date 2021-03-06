import secrets
from . import db
from datetime import datetime


class User(db.Model):
    __tablename__ = "user_data_auth"
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    role = db.Column(db.Boolean, nullable=False, default=False)
    superuser = db.Column(db.Boolean, nullable=False, default=False)
    password_hash = db.Column(db.String(256), nullable=False, unique=False)
    created_date = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, role=False, superuser=False,**kwargs):
        self.public_id = kwargs['public_id']
        self.username = kwargs['username']
        self.email = kwargs['email']
        self.password_hash = kwargs['password_hash']
        self.role = role
        self.superuser = superuser

    def __repr__(self):
        return '<User {}>'.format(self.username)
