from flask import Flask, g, make_response

import models
from resources.users import users_api
from resources.movies import movies_api
from flask_cors import CORS
from flask_login import (LoginManager, current_user, logout_user)
import config
import json
login_manager = LoginManager()


app = Flask(__name__)
app.secret_key = config.SECRET_KEY
login_manager.init_app(app)

@login_manager.user_loader
def load_user(userid):
		try:
			return models.User.get(models.User.id == userid)
		except models.DoesNotExist:
			return None


@app.route('/logout')
def get():
	logout_user()
	return 'logout successful'


@app.route('/')
def index():
	return 'hi'


@app.before_request
def before_request():
	"""Connect to the database before each request."""
	g.db = models.DATABASE
	g.db.connect()
	g.user = current_user

@app.after_request
def after_request(response):
	"""Close the database connection after each request."""
	g.db.close()
	return response


CORS(movies_api, origins= ["http://localhost:3000"], supports_credentials=True)
CORS(users_api, origins= ["http://localhost:3000"], supports_credentials=True)
app.register_blueprint(movies_api, url_prefix='/api/v1')
app.register_blueprint(users_api, url_prefix='/api/v1')



if __name__ == '__main__':
	models.initialize()
	app.run(debug=config.DEBUG, port=config.PORT)
