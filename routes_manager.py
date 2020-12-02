# flask packages
from flask_restful import Api
# project resources
from api.authentication import LoginApi, SignUpApi


def routes_creator(api: Api):
    api.add_resource(LoginApi, '/login/')
    api.add_resource(SignUpApi, '/signup/')