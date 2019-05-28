from flask import jsonify, Blueprint, abort
from flask_restful import (Resource, Api, reqparse, fields, marshal, marshal_with, url_for)

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
		return jsonify({'movies': [{'title': 'Leon the Professional'}, {'description': 'He cleaned'}]})

	@marshal_with(movie_fields)
	def post(self):
		args = self.reqparse.parse_args()
		print(args, 'hitting the post route boiiii')
		movie = models.Movie.create(**args)
		print(movie, "this is the movie")
		return (movie, 201)
		



class Movie(Resource):
	def get(self, id):
		return jsonify({'title': 'Leon the Professional'})

	def put(self, id):
		return jsonify({'title': 'Leon the Professional'})

	def delete(self, id):
		return jsonify({'title': 'Leon the Professional'})

movies_api = Blueprint('resources.movies', __name__)
api = Api(movies_api)
api.add_resource(
	MovieList,
	'/movies',
	endpoint='movies'
)
api.add_resource(
	Movie,
	'/movies/<int:id>',
	endpoint='movie'
)

