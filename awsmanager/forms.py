from awsmanager.documents import User
from flaskext import wtf
from flaskext.wtf import validators

class LoginForm(wtf.Form):
    username = wtf.TextField(u'Username', validators=[validators.Required()])
    password = wtf.PasswordField(u'Password', validators=[validators.Required(), validators.Length(min=6)])

    def validate_username(self, field):
        username = field.data
        password = self.password.data

        authenticated, user = User.query.authenticate(username, password)
        if not authenticated:
            raise validators.ValidationError("Login failed. Check your username and password.")
