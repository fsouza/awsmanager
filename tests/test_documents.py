import unittest
from awsmanager.documents import User
from nose.tools import assert_true

class TestDocuments(unittest.TestCase):

    def tearDown(self):
        for user in User.query.filter({}):
            user.remove()

    def test_should_be_able_to_authenticate_an_existing_user_with_right_password(self):
        user = User(username='tester')
        user.password = '123'
        user.save()

        authenticated, user = User.query.authenticate(username='tester', password='123')
        assert_true(authenticated)
