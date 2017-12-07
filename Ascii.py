from base import BaseHandler
from Art import Art
from google.appengine.ext import db

class AsciiHandler(BaseHandler):
	def render_front(self, title = "", art = "", error = ""):
		arts = db.GqlQuery("SELECT * FROM Art ORDER BY created DESC LIMIT 10")
		self.render("Templates/Ascii.html", title=title, art=art, error=error, arts = arts)

	def get(self):
		self.render_front()

	def post(self):
		title = self.request.get("title")
		art = self.request.get("art")
		if title == "clear" and art == "":
			b = Art(title = title, art = "art")
			arts = b.all()
			for art in arts:
				art.delete()
			self.render('Templates/Ascii.html')
		elif title and art:
			b = Art(title = title, art = art)
			b.put()
			self.render_front()
		else:
			error = "we need both a title and some artwork!"
			self.render("Templates/Ascii.html", title = title, art = art, error = error)

	def render_art(self):
		arts = db.GqlQuery("SELECT * FROM Art ORDER BY created DESC")
		self.render('Templates/Ascii.html', arts = arts)
