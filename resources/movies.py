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
		# models.Movie.select()
		# all_movies = models.Movie.select()
		# print(all_movies, "<--- the DB query for all_movies!")
		# new_movies = []


		# for movie in all_movies:
		# 	new_movies.append(marshal(movie, movie_fields))
		# g.user._get_current_object()
		# print(g.user._get_current_object())
		new_movies = [marshal(movie, movie_fields) for movie in models.Movie.select()]
		return new_movies


	@marshal_with(movie_fields)
	def post(self):
		#console.log(g.user._get_current_object(), "get _get_current_object in the post route")
		args = self.reqparse.parse_args()
		g.user = current_user
		print(args, 'hitting the post route')
		print(g.user._get_current_object())
		movie = models.Movie.create(created_by=1, **args)
		print(movie, "this is the movie")
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
		args = self.reqparse.parse_args()
		print(self.reqparse, '<=== self.reqparse')
		print(args)
		query = models.Movie.update(**args).where(models.Movie.id==id)
		query.execute()
		return (models.Movie.get(models.Movie.id==id), 200)

	def delete(self, id):
		query = models.Movie.delete().where(models.Movie.id==id)
		query.execute()
		return 'movie deleted amigo!'

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

