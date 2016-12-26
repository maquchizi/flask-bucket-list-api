from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from bucketlist import config

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)


class User(db.Model):
    """
    User
    """
    user_id = db.Column(db.Integer, primary_key=True)
    forename = db.Column(db.String(255))
    surname = db.Column(db.String(255))
    password = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    date_created = db.Column(db.DateTime())
    date_modified = db.Column(db.DateTime())

    def __init__(self, forename, email):
        self.forename = forename
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.forename


class Bucketlist(db.Model):
    """
    Bucketlist
    """
    list_id = db.Column(db.Integer, primary_key=True)
    list_title = db.Column(db.String(255))
    list_description = db.Column(db.String(255))
    created_by = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    items = db.relationship('BucketlistItem', backref='bucketlist',
                            lazy='dynamic')
    date_created = db.Column(db.DateTime())
    date_modified = db.Column(db.DateTime())


class BucketlistItem(db.Model):
    """
    BucketlistItem
    """
    item_id = db.Column(db.Integer, primary_key=True)
    item_content = db.Column(db.String(255))
    done = db.Column(db.Boolean(), default=False)
    bucketlist = db.Column(db.Integer, db.ForeignKey('bucketlist.list_id'))
    date_created = db.Column(db.DateTime())
    date_modified = db.Column(db.DateTime())


db.create_all()
