from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from bucketlist import config
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.sql import func

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
    _password = db.Column(db.LargeBinary)
    email = db.Column(db.String(255), unique=True)
    date_created = db.Column(db.DateTime(), server_default=func.now())
    date_modified = db.Column(db.DateTime(), server_default=func.now(),
                              onupdate=func.now())

    def __init__(self, forename, surname, password, email):
        self.forename = forename
        self.surname = surname
        self.password = password
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.forename

    @property
    def password(self):
        return self._password

    @property
    def id(self):
        return self.user_id

    @password.setter
    def password(self, password):
        self._password = generate_password_hash(password)

    def check_password(self, password):
        if check_password_hash(self._password, password):
            return True
        return False


class Bucketlist(db.Model):
    """
    Bucketlist
    """
    list_id = db.Column(db.Integer, primary_key=True)
    list_title = db.Column(db.String(255))
    list_description = db.Column(db.String(255))
    created_by = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    items = db.relationship('BucketlistItem', backref='list',
                            lazy='dynamic')
    date_created = db.Column(db.DateTime(), server_default=func.now())
    date_modified = db.Column(db.DateTime(), server_default=func.now(),
                              onupdate=func.now())

    def __init__(self, list_title, list_description, created_by):
        self.list_title = list_title
        self.list_description = list_description
        self.created_by = created_by


class BucketlistItem(db.Model):
    """
    BucketlistItem
    """
    item_id = db.Column(db.Integer, primary_key=True)
    item_content = db.Column(db.String(255))
    done = db.Column(db.Boolean(), default=False)
    bucketlist = db.Column(db.Integer, db.ForeignKey('bucketlist.list_id'))
    date_created = db.Column(db.DateTime(), server_default=func.now())
    date_modified = db.Column(db.DateTime(), server_default=func.now(),
                              onupdate=func.now())

    def __init__(self, item_content, bucketlist, done):
        self.item_content = item_content
        self.bucketlist = bucketlist
        self.done = done


db.create_all()
