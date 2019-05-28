import datetime

from peewee import *

DATABASE = SqliteDatabase('movies.sqlite')


class User(Model):
	username = CharField()
	password = CharField()
	created_at = DateTimeField(default=datetime.datetime.now)

	class Meta:
		database = DATABASE

class Movie(Model):
    title = CharField()
    description = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = DATABASE

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Movie], safe=True)
    DATABASE.close()