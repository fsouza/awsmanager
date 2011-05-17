import hashlib
from awsmanager import app, db
from flaskext.mongoalchemy import BaseQuery

class UserQuery(BaseQuery):

    def from_identity(self, identity):
        user = self.get(identity.name)
        identity.user = user
        return user

    def authenticate(self, username, password):
        user = self.filter({ 'username' : username}).first()

        if user:
            authenticated = user.check_password(password)
        else:
            authenticated = False

        return authenticated, user

class User(db.Document):
    username = db.StringField()
    password = db.StringField()

    def check_password(self, password):
        salt = app.config['PASSWORD_SALT']
        sha1 = hashlib.sha1()
        sha1.update(password)
        sha1.update(salt)
        return self.password == sha1.hexdigest()
