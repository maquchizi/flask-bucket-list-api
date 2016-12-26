from os import path

ROOT = path.dirname(path.realpath(__file__))
SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/flask-bucketlist'
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = 'supersecretkey'
DEBUG = True
