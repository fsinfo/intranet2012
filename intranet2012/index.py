from flask import *
from flask.views import MethodView
from flaskext.login import LoginManager, login_required, login_user, logout_user
from flask.ext.sqlalchemy import *

import ldap
from lib.ldapuser import LDAPUser

import json

from apps.addressbook.addressbook import addressbook

login_manager = LoginManager()
app = Flask(__name__)
app.debug = True
app.secret_key = 'foobar'
login_manager.setup_app(app)
login_manager.login_view = 'login'
#app.config.from_pyfile('test1.cfg')
#db = SQLAlchemy(app)

server = 'ldap://ford.fachschaft.cs.uni-kl.de'

l = ldap.initialize(server)

@login_manager.user_loader
def load_user(user_id):
	user = LDAPUser(l, user_id)
	if user.get_id:
		return user
	else:
		return None

@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	next = request.args.get('next')
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']

		user = LDAPUser(l, username)
		if user and password and user.authenticate(l, password):
			if login_user(user):
				flash("You have logged in")
				return redirect(next or url_for('home', error=error))
		error = "Login failed"
	return render_template('login.html', login=True, next=next, error=error)

@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('login'))

@app.route('/')
@login_required
def index():
	return render_template('index.html')

app.register_blueprint(addressbook, url_prefix='/addressbook')

if __name__ == '__main__':
	app.run()
