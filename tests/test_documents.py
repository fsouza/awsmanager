import unittest
from awsmanager.documents import User
from flaskext.principal import Identity
from nose.tools import assert_equals, assert_false, assert_true

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

    def test_should_be_able_to_not_authenticate_an_unexisting_user(self):
        authenticated, user = User.query.authenticate(username='unknown', password='wrong123')
        assert_false(authenticated)
        assert user is None

    def test_should_be_able_to_load_a_user_by_a_given_identity(self):
        identity = Identity(self.user.mongo_id)
        user = User.query.from_identity(identity)

        assert_equals(self.user, identity.user)
        assert_equals(self.user, user)
