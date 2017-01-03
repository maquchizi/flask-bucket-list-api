from flask import Flask
from bucketlist import config
from bucketlist.api import Api as API
from flask_restful import Api, Resource
from flask_jwt import JWT, jwt_required
from bucketlist.models import User

app = Flask(__name__)
app.config.from_object(config)
api = Api(app, catch_all_404s=True)
API = API()


def authenticate(email, password):
    user = User.query.filter_by(email=email).first()
    if user.check_password(password):
        return user
    return False


def identity(payload):
    user_id = payload['identity']
    return User.query.filter_by(user_id=user_id).first()


jwt = JWT(app, authenticate, identity)


class Register(Resource):
    """
    Register
    """
    def post(self):
        pass


class BucketlistItem(Resource):
    """
    BucketlistItem

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


class BucketList(Resource):
    """
    BucketList

    Handle all requests to /bucketlists
    """
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
api.add_resource(BucketList, '/bucketlists', '/bucketlists/<int:list_id>')
api.add_resource(BucketlistItem, '/bucketlists/<int:list_id>/items',
                 '/bucketlists/<int:list_id>/items/<int:item_id>')
api.add_resource(Register, '/auth/register')

if __name__ == '__main__':
    app.run(debug=True)
