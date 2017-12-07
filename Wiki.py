from base import BaseHandler
from Page import Page
from google.appengine.ext import db
from google.appengine.api import memcache



class WikiHandler(BaseHandler):
    def get(self, path):
        print(self)
        print("I happen!")
        p = Page.by_path(path).get()
        print(path)
        if p:
            self.render('Templates/Page.html', page = p, path = path)
        else:
            self.redirect('/_edit' + path)
