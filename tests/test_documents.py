import unittest
from awsmanager.documents import User
from nose.tools import assert_true, assert_false

class TestDocuments(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.user = User()
        cls.user.username = 'tester'
        cls.user.password = '123'
        cls.user.save()

    @classmethod
    def tearDownClass(cls):
        cls.user.remove()

    def test_should_be_able_to_authenticate_an_existing_user_with_right_password(self):
        authenticated, user = User.query.authenticate(username='tester', password='123')
        assert_true(authenticated)

    def test_should_be_able_to_not_authenticate_an_existing_user_with_wrong_password(self):
        authenticated, user = User.query.authenticate(username='tester', password='wrong123')
        assert_false(authenticated)
