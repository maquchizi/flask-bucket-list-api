from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from bucketlist import config

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)


@app.route('/')
def hello_world():
    return 'Hello, World!'
