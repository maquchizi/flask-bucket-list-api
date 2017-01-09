from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from flask_restful import reqparse, marshal, fields
from bucketlist import config
from bucketlist.models import User, Bucketlist, BucketlistItem
from flask_jwt import current_identity

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)


class AppAPI(object):

    def register(self):
        parser = reqparse.RequestParser()
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
            db.session.rollback()
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
            return {'bucketlist': response,
                    'message': 'Here is the list with ID %s'
                    % list_id}, 200
        else:
            return {'message': 'Bucketlist not found'}, 404

    def get_bucketlists(self):
        """
        Get all bucketlists belonging to logged in user
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
        bucketlists = Bucketlist.query.filter_by(created_by=current_identity.user_id).all()
        if bucketlists is not None:
            response = marshal(bucketlists, list_fields)
            return {'bucketlists': response,
                    'message': 'Here are all your lists'}, 200
        else:
            return {'message': 'No bucketlists found'}, 404

    def create_bucketlist(self, list_id):
        """
        Create a new bucketlist using posted data
        """
        if list_id:
            return {'message': 'This route was not found'}, 404

        parser = reqparse.RequestParser()
        parser.add_argument('list_title', required=True,
                            help="List title cannot be blank")
        parser.add_argument('list_description', required=True,
                            help="List description cannot be blank")
        args = parser.parse_args()

        list_fields = {
            "list_id": fields.String,
            "list_title": fields.String,
            "list_description": fields.String,
            "created_by": fields.String,
            "date_created": fields.DateTime(dt_format='rfc822'),
            "date_modified": fields.DateTime(dt_format='rfc822')
        }
        bucketlist = Bucketlist(args.list_title, args.list_description,
                                current_identity.user_id)
        db.session.add(bucketlist)
        db.session.commit()
        response = marshal(bucketlist, list_fields)
        return {'bucketlist': response, 'message':
                'New bucketlist created'}, 201

    def update_bucketlist(self, list_id):
        """
        Update bucketlist with given ID
        """
        if not list_id:
            return {'message': 'That list was not found'}, 404

        parser = reqparse.RequestParser()
        parser.add_argument('list_title', required=True,
                            help="List title cannot be blank")
        parser.add_argument('list_description')
        args = parser.parse_args()

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

        bucketlist = Bucketlist.query.filter_by(created_by=current_identity.user_id, list_id=list_id).first()
        if args.list_title:
            bucketlist.list_title = args.list_title
        if args.list_description:
            bucketlist.list_description = args.list_description

        db.session.commit()

        if bucketlist is not None:
            response = marshal(bucketlist, list_fields)
            return {'bucketlist': response,
                    'message':
                    'The bucketlist with ID %s was updated' % list_id}, 200
        else:
            return {'message': 'Bucketlist not found'}, 404

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
