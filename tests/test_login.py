import awsmanager
import unittest
from lxml import html
from nose.tools import assert_equals

class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client = awsmanager.app.test_client()

    def test_should_display_a_login_form_on_page(self):
        response = self.client.get('/login')
        assert_equals(200, response.status_code)

        dom = html.fromstring(response.data)
        assert_equals(1, len(dom.xpath('//input[@name="username"]')))
        assert_equals(1, len(dom.xpath('//input[@name="password"]')))
