import os

import webapp2
from NewPost import NewPostHandler
from Rot13 import Rot13Handler
from Birthday import BirthdayHandler
from Thanks import ThanksHandler
from Signup import SignupHandler
from Welcome import WelcomeHandler
from base import BaseHandler
from Ascii import AsciiHandler
from Blog import BlogHandler
from BlogPost import BlogPost
from Permalink import PermalinkHandler
from Login import LoginHandler
from Logout import LogoutHandler
from Flush import FlushHandler
from Wiki import WikiHandler
from Edit import EditHandler

from google.appengine.ext import db

class MainHandler(BaseHandler):
    def get(self):
        self.render('Templates/Main.html')

PAGE_RE = r'(/(?:[a-zA-Z0-9_-]+/?)*)'

app = webapp2.WSGIApplication([('/', MainHandler),
                                ('/birthday', BirthdayHandler),
                                ('/rot13', Rot13Handler),
                                ('/birthday/thanks', ThanksHandler),
                                # ('/', WikiHandler),
                                # ('/wiki/_edit/' + PAGE_RE, EditHandler),
                                # ('/_edit' + PAGE_RE, EditHandler),
                                ('/signup', SignupHandler),
                                ('/blog/welcome', WelcomeHandler),
                                ('/asciichan', AsciiHandler),
                                ('/blog/([0-9]+)(?:\.json)?', PermalinkHandler),
                                ('/blog/?(?:\.json)?', BlogHandler),
                                ('/blog/newpost', NewPostHandler),
                                ('/blog/flush', FlushHandler),
                                ('/login', LoginHandler),
                                ('/logout', LogoutHandler)
                                # (PAGE_RE, WikiHandler)
                                ],
    debug=True)
