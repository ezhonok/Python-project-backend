from flask import Flask, g

import models
from resources.users import users_api
from resources.movies import movies_api
from flask_cors import CORS
from flask_login import LoginManager
import config
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

CORS(movies_api, origins=["http://localhost:3000"], supports_credentials=True)
CORS(users_api, origins= ["http://localhost:3000"], supports_credentials=True)
app.register_blueprint(movies_api, url_prefix='/api/v1')
app.register_blueprint(users_api, url_prefix='/api/v1')





@app.route('/')
def index():
	return 'hi'

if __name__ == '__main__':
	models.initialize()
	app.run(debug=config.DEBUG, port=config.PORT)

@app.before_request
def before_request():
	"""Connect to the database before each request."""
	g.db = models.DATABASE
	g.db.connect()

@app.after_request
def after_request(response):
	"""Close the database connection after each request."""
	g.db.close()
	return response



