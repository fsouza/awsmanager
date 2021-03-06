import unittest
from awsmanager.documents import User
from awsmanager.forms import LoginForm
from nose.tools import assert_false, assert_true
from tests import app

class TestForms(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        with app.test_request_context():
            cls.user = User()
            cls.user.username = 'admin'
            cls.user.password = '123456'
            cls.user.save()

    @classmethod
    def tearDownClass(cls):
        cls.user.remove()

    def test_login_form_should_validate_presence_of_username(self):
        with app.test_request_context():
            form = LoginForm(username='', password='123')
            assert_false(form.validate())

    def test_login_form_should_validate_presence_of_password(self):
        with app.test_request_context():
            form = LoginForm(username='user', password=None)
            assert_false(form.validate())

    def test_login_form_should_validate_the_length_of_password(self):
        with app.test_request_context():
            form = LoginForm(username='user', password='12345')
            assert_false(form.validate())

    def test_login_form_should_accept_valid_username_and_password(self):
        with app.test_request_context():
            form = LoginForm(username='admin', password='123456')
            assert_true(form.validate())
