""" Exists at `/auth` and allows for authentication against Olin's LDAP server """

from flask import Blueprint, request
from flask_restful import Resource, Api

# Blueprint setup
auth = Blueprint('auth', __name__)
api = Api(auth)

class AuthedUser(Resource):
    """ Request a user profile, which will only be returned if that user can be
    successfully authenticated against Olin's LDAP server """

    def get(self):
        return "get"

    def post(self):
        return "post request with args = " + str(args) + "and sorted args = " + str(sorted(list(args)))


# Resources
api.add_resource(AuthedUser, '/') #url_prefix registered as /auth in src/app.py
