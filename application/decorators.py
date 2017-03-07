from application.settings import CREDENTIALS_DICT as credentials_dict
from application import flask_bcrypt
from flask import request, abort, jsonify, make_response


def authenticate_user(f):
    def check(*args, **kwargs):
        auth = request.authorization
        if auth:
            user_pass = credentials_dict.get(auth.username)
            if user_pass:
                is_valid = flask_bcrypt.check_password_hash(user_pass,
                                                            auth.password)
                if is_valid:
                    return f(*args, **kwargs)

        return abort(
            make_response(
                jsonify(
                    message="Not Authorised to the URL",
                    errorCode="authentication requied"),
                403))

    return check
