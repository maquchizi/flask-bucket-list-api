from datetime import timedelta
import os

try:
    environment = os.environ["ENV"]
except KeyError:
    os.environ["ENV"] = 'Production'
    environment = os.environ["ENV"]

if environment == 'Testing':
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'secret-key-is-secret'
    DEBUG = True
    JWT_DEFAULT_REALM = 'Login Required'
    JWT_AUTH_USERNAME_KEY = 'email'
    JWT_AUTH_URL_RULE = None
    JWT_EXPIRATION_DELTA = timedelta(seconds=3000)
    BUNDLE_ERRORS = True
else:
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/flask-bucketlist'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'secret-key-is-secret'
    DEBUG = True
    JWT_DEFAULT_REALM = 'Login Required'
    JWT_AUTH_USERNAME_KEY = 'email'
    JWT_AUTH_URL_RULE = None
    JWT_EXPIRATION_DELTA = timedelta(seconds=3000)
    BUNDLE_ERRORS = True
