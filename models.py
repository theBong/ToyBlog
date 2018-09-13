import datetime as dt
from peewee import *
db = SqliteDatabase('blog.db')

class Entry(Model):
	'''Content, timestamp, url-unique'''
	title = TextField(unique = True)
	content = TextField()
	timestamp = DateField(default=dt.datetime.now)

	class Meta:
		database = db


	
def initialize():
	db.connect()
	db.create_tables([Entry], safe = True)
	db.close()

