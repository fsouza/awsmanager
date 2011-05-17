# -*- coding: utf-8 -*-
import awsmanager
import mocker
from aws_mocks import MockCloudFrontConnection

class TestHome(mocker.MockerTestCase):

    def setUp(self):
        self.client = awsmanager.app.test_client()

    def tearDown(self):
        self.mocker.reset()

    def test_should_display_a_form_with_the_distributions_and_textarea_for_invalidate_paths(self):
        ConnectionManager = self.mocker.replace('awsmanager.util.ConnectionManager')
        ConnectionManager.get_cloudfront_connection()
        self.mocker.result(MockCloudFrontConnection())
        self.mocker.replay()

        response = self.client.get('/purge')
        for cname in ('static.domain.com', 'cdn.domain.uk'):
            assert cname in response.data

        self.mocker.verify()

    def test_should_invalidate_paths_on_amazon_cloudfront(self):
        paths = '/path/to/nowhere\n/path/to/anywhere'
        distribution = 'HD8932993S'

        ConnectionManager = self.mocker.replace('awsmanager.util.ConnectionManager')
        ConnectionManager.get_cloudfront_connection()
        self.mocker.result(MockCloudFrontConnection())
        self.mocker.replay()

        post_data = { 'paths' : paths, 'distribution' : distribution }
        response = self.client.post('/purge', data=post_data)

        for path in paths.split('\n'):
            assert ('<li>%s</li>' % path) in response.data

        self.mocker.verify()
