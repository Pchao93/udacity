import os
from base import BaseHandler
import Signup
import User
# from Signup import valid_username


class WelcomeHandler(BaseHandler):
    def get(self):
        if self.user:
            self.render('Templates/welcome.html', username = self.user.name)
        else:
            self.redirect('/signup')
