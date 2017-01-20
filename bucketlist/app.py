from flask import Flask
import config
from bucketlist.bucketlist_api import AppAPI
from flask_restful import Api, Resource, reqparse
from flask_jwt import JWT, jwt_required
from bucketlist.auth import Auth
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(config)
api = Api(app, catch_all_404s=True)
API = AppAPI()
auth = Auth()
jwt = JWT(app, auth.authenticate, auth.identity)
CORS(app)


class LoginAPI(Resource):
    """
    LoginAPI
    """
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('email', required=True,
                            help="Email cannot be blank")
        parser.add_argument('password', required=True,
                            help="Password cannot be blank")
        args = parser.parse_args()

        try:
            identity = jwt.authentication_callback(args.email, args.password)
        except AttributeError:
            return {'message': 'Invalid Credentials'}, 401

        if identity:
            access_token = jwt.jwt_encode_callback(identity)
            return jwt.auth_response_callback(access_token, identity)
        else:
            return {'message': 'Invalid Credentials'}, 401


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
    @jwt_required()
    def post(self, list_id=None):
        response = API.create_bucketlist_item(list_id)
        return response

    @jwt_required()
    def put(self, list_id=None, item_id=None):
        response = API.update_bucketlist_item(list_id, item_id)
        return response

    @jwt_required()
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

    @jwt_required()
    def put(self, list_id=None):
        response = API.update_bucketlist(list_id)
        return response

    @jwt_required()
    def delete(self, list_id=None):
        response = API.delete_bucketlist(list_id)
        return response


# Set up api routing
api.add_resource(BucketListAPI, '/bucketlists', '/bucketlists/<int:list_id>')
api.add_resource(BucketlistItemAPI, '/bucketlists/<int:list_id>/items',
                 '/bucketlists/<int:list_id>/items/<int:item_id>')
api.add_resource(RegisterAPI, '/auth/register')
api.add_resource(LoginAPI, '/auth/login')
