from flask import Flask
from .extensions import mongo, bcrypt


def create_app(config_object='source.settings', debug=False):
    app = Flask(__name__)
    if not debug:
        app.config.from_object(config_object)
    else:
        app.config["MONGO_URI"] = "mongodb://localhost:27017/atms"
    app.secret_key = 'some key that you will never guess'

    mongo.init_app(app)
    bcrypt.init_app(app)

    from .main import main
    app.register_blueprint(main)
    return app
