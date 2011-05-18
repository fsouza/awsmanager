import awsmanager
import unittest
from lxml import html
from nose.tools import assert_equals

class TestHome(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client = awsmanager.app.test_client()

    def test_show_contain_the_title_on_index(self):
        response = self.client.get('/')
        assert_equals(200, response.status_code)

        dom = html.fromstring(response.data)
        h1 = dom.xpath('//h1')[0]
        assert_equals('AWS Manager', h1.text)
