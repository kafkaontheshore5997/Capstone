# flask packages
from flask_restful import Api
# project resources
from api.authentication import LoginApi, SignUpApi
from api.markVisit import EnterStore


def routes_creator(api: Api):
    api.add_resource(EnterStore, '/enter/')
    api.add_resource(LoginApi, '/login/')
    api.add_resource(SignUpApi, '/signup/')

