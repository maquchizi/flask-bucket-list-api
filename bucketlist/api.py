from bucketlist.models import User, Bucketlist, BucketlistItem


class Api(object):

    def get_bucketlist(self, list_id):
        pass

    def get_bucketlists(self):
        pass

    def create_bucketlist(self, list_id):
        if list_id:
            return {'message': 'This route was not found'}, 404
        return {'bucketlist': 'New', 'message':
                'A new bucketlist was created'}, 201

    def update_bucketlist(self, list_id):
        pass

    def delete_bucketlist(self, list_id):
        pass
