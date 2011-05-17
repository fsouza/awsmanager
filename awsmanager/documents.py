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
    query_class = UserQuery

    username = db.StringField()
    hashed_password = db.StringField()

    def _encrypt(self, password):
        salt = app.config['PASSWORD_SALT']
        sha1 = hashlib.sha1()
        sha1.update(password)
        sha1.update(salt)
        return sha1.hexdigest()

    def check_password(self, password):
        return self.password == self._encrypt(password)

    def get_password(self):
        return self.hashed_password

    def set_password(self, password):
        self.hashed_password = self._encrypt(password)

    password = property(fget=get_password, fset=set_password)
