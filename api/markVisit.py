from flask import Response, request, jsonify
from mongoDB_model.user import Users
from mongoDB_model.visit import Visits
from flask_restful import Resource
from datetime import datetime


class EnterStore(Resource):
    @staticmethod
    def post() -> Response:
        body = request.get_json()
        username, store_name = body['username'], str(body['storeName'])

        user_info = Users.objects(username=username).first()
        if not user_info:
            return jsonify({"status": 'fail', "message": "Username doesn't exist. Please Sign up"})
        now = datetime.now()
        print(body, now)