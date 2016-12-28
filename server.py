from flask import Flask
from bucketlist import config
from bucketlist.api import Api as API
from flask_restful import Api, Resource

app = Flask(__name__)
app.config.from_object(config)
api = Api(app, catch_all_404s=True)
API = API()


class BucketlistItem(Resource):
    """
    BucketlsitItem
    """
    def post(self, list_id):
        print(list_id)

    def put(self, list_id, item_id):
        print(list_id)
        print(item_id)

    def delete(self, list_id, item_id):
        print(list_id)
        print(item_id)


class BucketList(Resource):
    """docstring for BucketList"""
    def post(self, list_id=None):
        response = API.create_bucketlist(list_id)
        return response

    def get(self, list_id=None):
        print('Something')

    def put(self, list_id):
        pass

    def delete(self, list_id):
        pass


# Set up api routing
api.add_resource(BucketList, '/bucketlists', '/bucketlists/<int:list_id>')
api.add_resource(BucketlistItem, '/bucketlists/<int:list_id>/items',
                 '/bucketlists/<int:list_id>/items/<int:item_id>')

if __name__ == '__main__':
    app.run()
