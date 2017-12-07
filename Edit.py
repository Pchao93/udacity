from Page import Page
from base import BaseHandler
from google.appengine.ext import db
from google.appengine.api import memcache
import re

class EditHandler(BaseHandler):
    def get(self, path):
        if not self.user:
            self.redirect('/login')
        p = Page.by_path(path).get()
        self.render('Templates/NewPage.html', page = p)

    def post(self, path):
        if not self.user:
            self.error(400)
            return

        content = self.request.get("content")
        old_page = Page.by_path(path).get()
        if  not (old_page or content):
            return
        elif not old_page or old_page.content != content:
            p = Page(parent = Page.parent_key(path), content = content)
            p.put()
        else:
            path = re.sub('\_edit$', '', path)
            self.redirect(path)
