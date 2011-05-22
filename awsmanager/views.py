from awsmanager.forms import LoginForm
from awsmanager.util import ConnectionManager
from flask import Module, render_template, request

frontend = Module(__name__)

@frontend.route('/')
def index():
    return render_template("index.html")

@frontend.route('/purge')
def show_purge_form():
    connection = ConnectionManager.get_cloudfront_connection()
    distributions = connection.get_all_distributions()
    return render_template("purge_form.html", distributions=distributions)

@frontend.route('/purge', methods=['POST'])
def purge_paths():
    distribution_id = request.form['distribution']
    paths = [p.strip() for p in request.form['paths'].split('\n')]
    connection = ConnectionManager.get_cloudfront_connection()
    batch = connection.create_invalidation_request(distribution_id, paths)
    return render_template("invalidation_sent.html", batch=batch)

@frontend.route('/login')
def show_login_form():
    form = LoginForm()
    return render_template("login.html", form=form)

@frontend.route('/login', methods=['POST'])
def do_login():
    form = LoginForm()
    if form.validate_on_submit():
        pass
        # TODO: login
    return render_template("login.html", form=form)
