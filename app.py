from flask_restful import Api
from flask import Flask
from flask_mongoengine import MongoEngine
import routes_manager

CONN_STR = 'mongodb+srv://Capstone:1234@cluster0.mvxpf.mongodb.net/test'
db = MongoEngine()


# initialize flask and db
def create_app(config=None):
    flask_app = Flask(__name__)
    if config is not None:
        flask_app.config.from_object(config)

    db.init_app(flask_app)

    @flask_app.route('/')
    def index():
        return "Hello World!"
    # init api and routes
    api = Api(app=flask_app)
    routes_manager.routes_creator(api=api)

    return flask_app


if __name__ == '__main__':
    app = create_app(config='config')
    app.run(debug=True, host='0.0.0.0')
