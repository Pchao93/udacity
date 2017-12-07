from base import BaseHandler
from BlogPost import BlogPost
from google.appengine.ext import db
from google.appengine.api import memcache
import time

class PermalinkHandler(BaseHandler):
    def get(self, postid):

        post = most_recent_post(postid)
        print(post)

        if self.format == 'html':
            if memcache.get("PERMALINK_LAST_QUERIED") is None:
                memcache.set("PERMALINK_LAST_QUERIED", time.time())
            diff = time.time() - memcache.get("PERMALINK_LAST_QUERIED")
            self.render('Templates/Permalink.html', post = post, time = diff)
        else:
            self.render_json(posts.get().as_dict())


def most_recent_post(postid):
    key = postid
    post = memcache.get(key)
    if post is None:
        # post = db.GqlQuery("SELECT * "
        #                     "FROM BlogPost "
        #                     "ORDER BY created DESC "
        #                     "LIMIT 10")
        _key = db.Key.from_path('BlogPost', int(postid))
        post = db.get(_key)
        memcache.set(key, post)
        memcache.set("PERMALINK_LAST_QUERIED", time.time())
    return post
