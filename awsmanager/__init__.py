from awsmanager.views import frontend
from flask import Flask
from flaskext.mongoalchemy import MongoAlchemy

db = MongoAlchemy()

def get_app(settings_module='awsmanager.settings'):
    app = Flask(__name__)
    app.config.from_object(settings_module)

    app.register_module(frontend)

    db.init_app(app)

    return app

import views
