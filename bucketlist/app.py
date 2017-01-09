from flask import Flask
from bucketlist import config
from bucketlist.bucketlist_api import AppAPI
from flask_restful import Api, Resource
from flask_jwt import JWT, jwt_required, current_identity
from bucketlist.auth import Auth

app = Flask(__name__)
app.config.from_object(config)
api = Api(app, catch_all_404s=True)
API = AppAPI()
auth = Auth()
jwt = JWT(app, auth.authenticate, auth.identity)


class RegisterAPI(Resource):
    """
    RegisterAPI
    """
    def post(self):
        response = API.register()
        return response


class BucketlistItemAPI(Resource):
    """
    BucketlistItemAPI

    Handle all requests to /bucketlists/<int:list_id>/items/<int:item_id>
    """
    def post(self, list_id=None):
        response = API.create_bucketlist_item(list_id)
        return response

    def put(self, list_id=None, item_id=None):
        response = API.update_bucketlist_item(list_id, item_id)
        return response

    def delete(self, list_id=None, item_id=None):
        response = API.delete_bucketlist_item(list_id, item_id)
        return response


class BucketListAPI(Resource):
    """
    BucketListAPI

    Handle all requests to /bucketlists
    """
    @jwt_required()
    def post(self, list_id=None):
        response = API.create_bucketlist(list_id)
        return response

    @jwt_required()
    def get(self, list_id=None):
        if not list_id:
            response = API.get_bucketlists()
        else:
            response = API.get_bucketlist(list_id)
        return response

    def put(self, list_id=None):
        response = API.update_bucketlist(list_id)
        return response

    def delete(self, list_id=None):
        response = API.delete_bucketlist(list_id)
        return response


# Set up api routing
api.add_resource(BucketListAPI, '/bucketlists', '/bucketlists/<int:list_id>')
api.add_resource(BucketlistItemAPI, '/bucketlists/<int:list_id>/items',
                 '/bucketlists/<int:list_id>/items/<int:item_id>')
api.add_resource(RegisterAPI, '/auth/register')

if __name__ == '__main__':
    app.run(debug=True)
