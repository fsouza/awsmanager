from flaskext import wtf
from flaskext.wtf import validators

class LoginForm(wtf.Form):
    username = wtf.TextField(u'Username', validators=[validators.Required()])
    password = wtf.PasswordField(u'Password', validators=[validators.Required()])
