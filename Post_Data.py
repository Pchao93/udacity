import webapp2

from google.appengine.ext import db

POST_COUNT = 0

class Post(db.Model):
	subject = db.StringProperty(required = True)
	content = db.TextProperty(required = True)
	created = db.DateTimeProperty(auto_now_add = True)
	post_id = db.IntegerProperty(required=True)
