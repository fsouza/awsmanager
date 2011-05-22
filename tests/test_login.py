import unittest
from awsmanager.documents import User
from lxml import html
from nose.tools import assert_equals
from tests import app

class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        with app.test_request_context():
            cls.client = app.test_client()
            cls.user = User()
            cls.user.username = 'admin'
            cls.user.password = '123456'
            cls.user.save()

    @classmethod
    def tearDownClass(cls):
        cls.user.remove()

    def test_should_display_a_login_form_on_page(self):
        response = self.client.get('/login')
        assert_equals(200, response.status_code)

        dom = html.fromstring(response.data)
        assert_equals(1, len(dom.xpath('//input[@name="username"]')))
        assert_equals(1, len(dom.xpath('//input[@name="password"]')))

    def test_should_display_validation_errors_on_login_failure(self):
        data = {
            'username' : 'admin',
            'password' : '',
        }

        response = self.client.post('/login', data=data, follow_redirects=True)
        assert_equals(200, response.status_code)

        assert 'required' in response.data

    def test_should_be_able_to_login_with_right_data(self):
        data = {
            'username' : 'admin',
            'password' : '123456',
        }

        response = self.client.post('/login', data=data, follow_redirects=True)
        assert_equals(200, response.status_code)

        dom = html.fromstring(response.data)
        assert_equals("AWS Manager", dom.xpath("//h1")[0].text)
