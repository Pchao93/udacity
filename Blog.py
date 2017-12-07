from base import BaseHandler
from BlogPost import BlogPost
from google.appengine.ext import db
from google.appengine.api import memcache
import time

class BlogHandler(BaseHandler):
    def get(self):
        posts = most_recent_posts()
        print(posts)

        if self.format == 'html':
            print("only I happen!")
            if memcache.get("BLOG_LAST_QUERIED") is None:
                memcache.set("BLOG_LAST_QUERIED", time.time())
            diff = time.time() - memcache.get("BLOG_LAST_QUERIED")
            self.render('Templates/Blog.html', posts = posts, time = diff)
        else:
            return self.render_json([p.as_dict() for p in posts])


def most_recent_posts(update = False):
    key = 'front'
    posts = memcache.get(key)
    print(posts)
    print(posts is None)
    if posts == [] or update:
        print("I happen!")
        posts = db.GqlQuery("SELECT * FROM BlogPost ORDER BY created DESC LIMIT 10")
        posts = list(posts)
        memcache.set(key, posts)
        memcache.set("BLOG_LAST_QUERIED", time.time())
        print("I happen!")
    return posts
