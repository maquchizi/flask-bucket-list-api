from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from bucketlist import config

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)


class User(db.model):
    """
    User
    """
    user_id = db.Column(db.Integer, primary_key=True)
    forename = db.Column(db.String(255))
    surname = db.Column(db.String(255))
    password = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    created = db.Column(db.DateTime())
    modified = db.Column(db.DateTime())

    def __init__(self, forename, email):
        self.forename = forename
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.forename


class Bucketlist(db.model):
    """
    Bucketlist
    """
    list_id = db.Column(db.Integer, primary_key=True)
    list_name = db.Column(db.String(255))
    list_description = db.Column(db.String(255))
    user = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    created = db.Column(db.DateTime())
    modified = db.Column(db.DateTime())


class BucketlistItem(object):
    """
    BucketlistItem
    """
    item_id = db.Column(db.Integer, primary_key=True)
    bucketlist = db.Column(db.Integer, db.ForeignKey('bucketlist.list_id'))
    created = db.Column(db.DateTime())
    modified = db.Column(db.DateTime())
