from flask import Flask

import config
from .database import db


def create_app():
    app = Flask(__name__)
    app.config.from_object(config.DevelopmentConfig)

    db.init_app(app)
    with app.test_request_context():
        db.create_all()

    import app.module.views as module
    import app.module.api as module_api

    app.register_blueprint(module.views)
    app.register_blueprint(module_api.api_route)

    return app
