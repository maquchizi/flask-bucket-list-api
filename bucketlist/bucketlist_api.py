from flask import Flask
from sqlalchemy.exc import IntegrityError
from flask_restful import reqparse, marshal
from bucketlist import config
from bucketlist.models import db, User, Bucketlist, BucketlistItem
from flask_jwt import current_identity
from serialize_fields import list_fields, list_fields_without_items

app = Flask(__name__)
app.config.from_object(config)


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

        # Enforce the unique email address constraint
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
        # Get bucketlist item by ID only if it was created
        # by the currently logged in user
        bucketlist = Bucketlist.query.filter_by(
            created_by=current_identity.user_id, list_id=list_id).first()
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
        # Get bucketlists created by the currently logged in user
        bucketlists = Bucketlist.query.filter_by(
            created_by=current_identity.user_id).all()
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

        # Create bucketlist from POST data
        bucketlist = Bucketlist(args.list_title, args.list_description,
                                current_identity.user_id)
        db.session.add(bucketlist)
        db.session.commit()

        response = marshal(bucketlist, list_fields_without_items)
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

        bucketlist = Bucketlist.query.filter_by(
            created_by=current_identity.user_id, list_id=list_id).first()
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

        # Delete only if list os owned by currently logged in user
        bucketlist = Bucketlist.query.filter_by(
            created_by=current_identity.user_id, list_id=list_id).first()

        if bucketlist is not None:
            db.session.delete(bucketlist)
            db.session.commit()

            return {'message':
                    'The bucketlist with ID %s was deleted' % list_id}, 200
        else:
            return {'message': 'Bucketlist not found'}, 404

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
