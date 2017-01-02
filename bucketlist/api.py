from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from bucketlist import config
from bucketlist.models import User, Bucketlist, BucketlistItem

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)


class Api(object):

    def get_bucketlist(self, list_id):
        """
        Get a single bucketlist selected by ID
        """
        return {'message': 'Here is the list with ID %s' % list_id}, 200

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
