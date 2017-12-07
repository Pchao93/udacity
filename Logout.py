from base import BaseHandler
from User import User

class LogoutHandler(BaseHandler):
    def get(self):
        self.logout()
        self.redirect('/')
