from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from flask_restful import reqparse, marshal, fields
from bucketlist import config
from bucketlist.models import User, Bucketlist, BucketlistItem

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)
parser = reqparse.RequestParser()


class AppAPI(object):

    def register(self):
        parser.add_argument('forename', required=True,
                            help="Forename cannot be blank")
        parser.add_argument('surname', required=True,
                            help="Surname cannot be blank")
        parser.add_argument('email', required=True,
                            help="Email cannot be blank")
        parser.add_argument('password', required=True,
                            help="Password cannot be blank")
        args = parser.parse_args()
        try:
            user = User(args.forename, args.surname, args.password, args.email)
            db.session.add(user)
            db.session.commit()
            return {'message': 'New user created'}, 201
        except IntegrityError:
            return {'message': 'That email address is already taken'}, 400

    def get_bucketlist(self, list_id):
        """
        Get a single bucketlist selected by ID
        """
        item_fields = {
            "item_id": fields.String,
            "item_content": fields.String,
            "done": fields.Boolean,
            "date_created": fields.DateTime(dt_format='rfc822'),
            "date_modified": fields.DateTime(dt_format='rfc822')
        }
        list_fields = {
            "list_id": fields.String,
            "list_title": fields.String,
            "list_description": fields.String,
            "items": fields.Nested(item_fields),
            "created_by": fields.String,
            "date_created": fields.DateTime(dt_format='rfc822'),
            "date_modified": fields.DateTime(dt_format='rfc822')
        }
        bucketlist = Bucketlist.query.filter_by(list_id=list_id).first()
        if bucketlist is not None:
            response = marshal(bucketlist, list_fields)
            return {'list': response, 'message': 'Here is the list with ID %s'
                    % list_id}, 200
        else:
            return {'message': 'Bucketlist not found'}, 404

    def get_bucketlists(self):
        """
        Get all bucketlists belonging to logged in user
        """
        return {'message': 'Here are all your lists'}

    def create_bucketlist(self, list_id):
        """
        Create a new bucketlist using posted data
        """
        if list_id:
            return {'message': 'This route was not found'}, 404
        return {'bucketlist': 'New', 'message':
                'A new bucketlist was created'}, 201

    def update_bucketlist(self, list_id):
        """
        Update bucketlist with given ID
        """
        if not list_id:
            return {'message': 'That list was not found'}, 404
        return {'message':
                'The bucketlist with ID %s was updated' % list_id}, 200

    def delete_bucketlist(self, list_id):
        """
        Delete bucketlist with given ID
        """
        if not list_id:
            return {'message': 'That list was not found'}, 404
        return {'message':
                'The bucketlist with ID %s was deleted' % list_id}, 200

    def create_bucketlist_item(self, list_id):
        """
        Create a new item in the list specified by list_id
        """
        if not list_id:
            return {'message': 'That list was not found'}, 404
        return {'message':
                'Item created in bucketlist with ID %s' % list_id}, 201

    def update_bucketlist_item(self, list_id, item_id):
        """
        Update a list item with id item_id

        The item must be in the list specified by list_id
        """
        if not item_id:
            return {'message': 'That item was not found'}, 404
        return {'message':
                'Item with ID %s was updated' % item_id}, 200

    def delete_bucketlist_item(self, list_id, item_id):
        """
        Delete a list item with id item_id

        The item must be in the list specified by list_id
        """
        if not item_id:
            return {'message': 'That item was not found'}, 404
        return {'message':
                'Item with ID %s was deleted' % item_id}, 200
