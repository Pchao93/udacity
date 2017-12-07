from base import BaseHandler
from google.appengine.api import memcache


class FlushHandler(BaseHandler):

    def get(self):
        memcache.flush_all()
        self.redirect('/blog')
