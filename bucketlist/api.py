from bucketlist.models import User, Bucketlist, BucketlistItem


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
