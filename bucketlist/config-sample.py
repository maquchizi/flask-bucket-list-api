from os import path

ROOT = path.dirname(path.realpath(__file__))
SQLALCHEMY_DATABASE_URI = 'postgres://username:password@server/flask-bucketlist'
SECRET_KEY = 'supersecretkey'
DEBUG = True
