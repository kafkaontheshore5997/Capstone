from app import db
import datetime


class Visits(db.Document):
    storeName = db.StringField(required=True)
    username = db.StringField(required=True, unique=True)
    enterTime = db.DateTimeField(required=False, default=datetime.datetime.utcnow)
    exitTime = db.DateTimeField(required=False, default=datetime.datetime.utcnow)
