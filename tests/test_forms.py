import awsmanager
import unittest
from awsmanager.forms import LoginForm
from nose.tools import assert_false

class TestForms(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        awsmanager.app.config['CSRF_ENABLED'] = False

    @classmethod
    def tearDownClass(cls):
        awsmanager.app.config['CSRF_ENABLED'] = True

    def test_login_form_should_validate_presence_of_username(self):
        with awsmanager.app.test_request_context():
            form = LoginForm(username='', password='123')
            assert_false(form.validate())
