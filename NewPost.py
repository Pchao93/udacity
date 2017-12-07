import time
from BlogPost import BlogPost
from base import BaseHandler
from Blog import most_recent_posts
from Permalink import most_recent_post
from google.appengine.ext import db
from google.appengine.api import memcache

class NewPostHandler(BaseHandler):


    def get(self):
        self.render('Templates/NewPost.html')

    def post(self):
        subject = self.request.get("subject")
        content = self.request.get("content")
        if subject == "$clear" and content == "":
            b = BlogPost(subject = subject, content = "content")
            posts = b.all()
            for post in posts:
                post.delete()
            memcache.flush_all()
            memcache.set("LAST_QUERIED", time.time())

            self.redirect('/blog')
        elif subject and content:
            b = BlogPost(subject = subject, content = content)
            b.put()
            most_recent_posts(True)
            self.redirect('/blog/%s' % str(b.key().id()))
        else:
            error = "we need both a subject and some content!"
            self.render("Templates/NewPost.html", subject = subject, content = content, error = error)
