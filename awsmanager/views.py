from awsmanager import app
from awsmanager.forms import LoginForm
from awsmanager.util import ConnectionManager
from flask import render_template, request

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

@app.route('/login')
def show_login_form():
    form = LoginForm()
    return render_template("login.html", form=form)
