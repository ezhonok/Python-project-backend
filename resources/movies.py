from flask import jsonify, Blueprint, abort, g
from flask_restful import (Resource, Api, reqparse, fields, marshal, marshal_with, url_for)
from flask_login import (LoginManager, current_user)

import models

# Define fields on responses
movie_fields = {
	'id': fields.Integer,
	'title': fields.String,
	'description': fields.String,
}



class MovieList(Resource):
	def __init__(self):
		self.reqparse = reqparse.RequestParser()
		self.reqparse.add_argument(
			'title',
			required=False,
			help='No dog title provided',
			location=['form', 'json']
		)
		self.reqparse.add_argument(
			'description',
			required=False,
			help='No description provided',
			location=['form', 'json']
		)
		super().__init__()

	def get(self):
		# g.user._get_current_object()
		# print(g.user._get_current_object())
		new_movies = [marshal(movie, movie_fields) for movie in models.Movie.select()]
		return new_movies


	@marshal_with(movie_fields)
	def post(self):
		args = self.reqparse.parse_args()
		g.user = current_user
		createdMovsUserId = g.user._get_current_object()
		movie = models.Movie.create(created_by=createdMovsUserId, **args)
		print(movie, "<=== movie in the post route")
		print(movie.created_by, "<=== created_by in the post route")
		return (movie, 201)




class Movie(Resource):


	def __init__(self):
		self.reqparse = reqparse.RequestParser()
		self.reqparse.add_argument(
			'title',
			required=False,
			help='No movie title provided',
			location=['form', 'json']
		)
		self.reqparse.add_argument(
			'description',
			required=False,
			help='No description provided',
			location=['form', 'json']
		)
		super().__init__()

	@marshal_with(movie_fields)
	def get(self, id):
		return (movie, 201)

	@marshal_with(movie_fields)
	def put(self, id):
		g.user = current_user
		args = self.reqparse.parse_args()
		query = models.Movie.update(**args).where(models.Movie.id==id)
		print(query)
		query.execute()
		return (models.Movie.get(models.Movie.id==id), 200)

	def delete(self, id):
		g.user = current_user
		print(g.user, "<-- g.user")
		movieToDelete = models.Movie.get(models.Movie.id==id)
		print(movieToDelete, "<=-=-= movieToDelete")
		print(movieToDelete.created_by, "<---- movieToDelete.created_by")
		if movieToDelete.created_by == g.user:
			query = models.Movie.delete().where(models.Movie.id==id)
			query.execute()
			return ("creator id match")
		else:
			return ("creator id fail")


movies_api = Blueprint('resources.movies', __name__)
api = Api(movies_api)
api.add_resource(
	MovieList,
	'/movies'
)

api.add_resource(
	Movie,
	'/movies/<int:id>'
)

