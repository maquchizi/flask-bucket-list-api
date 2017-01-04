from bucketlist.models import User


class Auth(object):
    def authenticate(self, email, password):
        user = User.query.filter_by(email=email).first()
        if user.check_password(password):
            return user
        return False

    def identity(self, payload):
        user_id = payload['identity']
        return User.query.filter_by(user_id=user_id).first()
