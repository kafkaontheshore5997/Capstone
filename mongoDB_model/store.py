from app import db


class Stores(db.Document):
    storeName = db.StringField(required=True, unique=True)
    address = db.StringField(required=True)