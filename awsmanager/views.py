from awsmanager import app
from boto.cloudfront import CloudFrontConnection
from flask import render_template, request

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

@app.route('/purge', methods=['POST'])
def purge_paths():
    distribution_id = request.form['distribution']
    paths = [p.strip() for p in request.form['paths'].split('\n')]
    connection = ConnectionManager.get_cloudfront_connection()
    batch = connection.create_invalidation_request(distribution_id, paths)
    return render_template("invalidation_sent.html", batch=batch)
