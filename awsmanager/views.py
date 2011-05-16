from awsmanager import app
from boto.cloudfront import CloudFrontConnection
from flask import render_template

class ConnectionManager(object):
    _connection = None

    @classmethod
    def get_cloudfront_connection(cls):
        if cls._connection is None:
            cls._connection = CloudFrontConnection(
                                    aws_access_key_id=app.config['AWS_ACCESS_KEY_ID'],
                                    aws_secret_access_key=app.config['AWS_SECRET_ACCESS_KEY'])
        return cls._connection

@app.route('/purge')
def show_purge_form():
    connection = ConnectionManager.get_cloudfront_connection()
    distributions = connection.get_all_distributions()
    return render_template("purge_form.html", distributions=distributions)
