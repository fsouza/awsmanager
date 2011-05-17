import mocker
from awsmanager import app
from nose.tools import assert_equals

class TestUtil(mocker.MockerTestCase):

    def tearDown(self):
        self.mocker.reset()

    def test_should_get_connection_to_amazon_cloudfront_using_boto(self):
        CloudFrontConnection = self.mocker.replace('boto.cloudfront.CloudFrontConnection')
        CloudFrontConnection(aws_access_key_id=app.config['AWS_ACCESS_KEY_ID'], aws_secret_access_key=app.config['AWS_SECRET_ACCESS_KEY'])
        self.mocker.result('connected')
        self.mocker.replay()

        from awsmanager.util import ConnectionManager
        connection = ConnectionManager.get_cloudfront_connection()
        assert_equals('connected', connection)
        self.mocker.verify()
