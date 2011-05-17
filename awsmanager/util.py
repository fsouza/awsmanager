from awsmanager import app
from boto.cloudfront import CloudFrontConnection

class ConnectionManager(object):
    _connection = None

    @classmethod
    def get_cloudfront_connection(cls):
        if cls._connection is None:
            cls._connection = CloudFrontConnection(
                                    aws_access_key_id=app.config['AWS_ACCESS_KEY_ID'],
                                    aws_secret_access_key=app.config['AWS_SECRET_ACCESS_KEY'])
        return cls._connection

