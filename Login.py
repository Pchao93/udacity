from base import BaseHandler
from User import User

class LoginHandler(BaseHandler):
    def get(self):
        next_url = self.request.headers.get('referer', '/')
        self.render('Templates/Login.html', next_url = next_url)

    def post(self):

        next_url = str(self.request.get('next_url'))
        if not next_url or next_url.startswith('login'):
            next_url = '/'

        username = self.request.get('username')
        password = self.request.get('password')

        u = User.login(username, password)
        if u:
            self.login(u)
            self.redirect(next_url)
        else:
            msg = 'Invalid login'
            self.render('Templates/Login.html', error = msg)
