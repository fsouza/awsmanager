from awsmanager.views import frontend
from flask import Flask

def get_app(settings_module='awsmanager.settings'):
    app = Flask(__name__)
    app.config.from_object(settings_module)

    app.register_module(frontend)

    return app

import views
