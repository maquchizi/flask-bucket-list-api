from os import path
from datetime import timedelta

ROOT = path.dirname(path.realpath(__file__))
SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/flask-bucketlist'
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = 'supersecretkey'
DEBUG = True
JWT_DEFAULT_REALM = 'Login Required'
JWT_AUTH_USERNAME_KEY = 'email'
JWT_AUTH_URL_RULE = '/auth/login'
JWT_EXPIRATION_DELTA = timedelta(seconds=3000)
BUNDLE_ERRORS = True
