import os
from base import BaseHandler

from google.appengine.ext import db


class Rot13Handler(BaseHandler):
    def get(self):
        self.render('Templates/rot13-form.html')

    def post(self):
        rot13 = ''
        text = self.request.get('text')
        if text:
            rot13 = text.encode('rot13')

        self.render('Templates/rot13-form.html', text = rot13)
