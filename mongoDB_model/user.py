from app import db


class Users(db.Document):
    username = db.StringField(required=True, unique=True)
    password = db.StringField(required=True)
    email = db.EmailField(required=True)