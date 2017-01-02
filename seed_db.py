from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from bucketlist import config
from bucketlist.models import User, Bucketlist, BucketlistItem

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)

mark = User('Mark', 'Ng\'ang\'a', 'p@ssw0rd', 'mark.nganga@andela.com')
db.session.add(mark)
db.session.commit()

bucketlist = Bucketlist('First List', 'Just for kicks', mark.user_id)
db.session.add(bucketlist)
db.session.commit()

list_item = BucketlistItem('Do all the things', bucketlist.list_id, False)
db.session.add(list_item)
db.session.commit()
