from flask import Flask
from flaskext.mongoalchemy import MongoAlchemy

app = Flask(__name__)
app.config.from_object('awsmanager.settings')
db = MongoAlchemy(app)

import views
