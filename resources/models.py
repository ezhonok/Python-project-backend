import datetime

from peewee import *


DATABASE = PostgresqlDatabase('movies', user='lanaetgreg', password='password')

class User(UserMixin, Model):
    username = CharField(unique=True)
    email    = CharField(unique=True)
    password = CharField()

    class Meta:
        database = DATABASE

    @classmethod
    def create_user(cls, username, email, password, **kwargs):
        email = email.lower()
        try:
            cls.select().where(
                (cls.email==email)
            ).get()
        except cls.DoesNotExist:
            user = cls(username=username, email=email)
            user.password = generate_password_hash(password)
            user.save()
            return user
        else:
            raise Exception("user with this email already exists")






class Movie(Model):
    title = CharField()
    description = TextField()
    created_by = ForeignKeyField(User, related_name='movie_set')
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = DATABASE



class User(Model):
	username = CharField()
	password = CharField()
	created_at = DateTimeField(default=datetime.datetime.now)

	class Meta:
		database = DATABASE


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Movie], safe=True)
    DATABASE.close()