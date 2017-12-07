import os
import re
import random
import string
import hashlib
from base import BaseHandler
from User import User
from google.appengine.ext import db

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
    return username and USER_RE.match(username)

PASS_RE = re.compile(r"^.{3,20}$")
def valid_password(password):
    return password and PASS_RE.match(password)

EMAIL_RE  = re.compile(r'^[\S]+@[\S]+\.[\S]+$')
def valid_email(email):
    return not email or EMAIL_RE.match(email)

secret = 'secret'

def make_secure_val(val):
    return '%s|%s' % (val, hmac.new(secret, val).hexdigest())

def check_secure_val(secure_val):
    val = secure_val.split('|')[0]
    if secure_val == make_secure_val(val):
        return val

class SignupHandler(BaseHandler):
    def get(self):
        next_url = self.request.headers.get('referer', '/')
        self.render('Templates/Signup.html', next_url = next_url)

    def post(self):
        have_error = False
        next_url = str(self.request.get('next_url'))
        if not next_url or next_url.startswith('login'):
            next_url = '/'

        username = self.request.get('Username')
        password = self.request.get('Password')
        verify = self.request.get('Verify')

        params = dict(username = username)

        if not valid_username(username):
            params['username_error'] = "That's not a valid username."
            have_error = True

        if not valid_password(password):
            params['password_error'] = "That wasn't a valid password."
            have_error = True
        elif password != verify:
            params['match_error'] = "Your passwords didn't match."
            have_error = True

        if have_error:
            self.render('Templates/Signup.html', **params)
        else:
            u = User.by_name(username)
            if u:
                msg = 'That user already exists.'
                self.render('Templates/Signup.html', username_error = msg)
            else:
                u = User.register(username, password)
                u.put()

                self.login(u)
                self.redirect('next_url')
