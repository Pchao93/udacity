import os
from base import BaseHandler

class ThanksHandler(BaseHandler):
    def get(self):
        self.render('Templates/thanks.html')