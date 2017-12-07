import os
from base import BaseHandler
from string import letters

from google.appengine.ext import db

class BirthdayHandler(BaseHandler):
    
    def write_form(self, error="", month="", day="", year=""):
        self.response.out.write(form % {"error" : escape_html(error),
                                        "month" : escape_html(month),
                                        "day" : escape_html(day),
                                        "year" : escape_html(year)})

    def get(self):
        self.render('Templates/Birthday.html', month = "Month", day = "Day", year = "Year")

    def post(self):
        user_month = self.request.get('month')
        user_day = self.request.get('day')
        user_year = self.request.get('year')

        month = self.valid_month(user_month)
        day = self.valid_day(user_day)
        year = self.valid_year(user_year)

        if not(month and day and year):
            self.render('Templates/Birthday.html', month = user_month, day = user_day, year = user_year, error = "Invalid date. Please try again!")
        else:
            self.redirect("/birthday/thanks")

    months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']

    def valid_month(self, month):
        if month and month.capitalize() in self.months:
            return month.capitalize()
        return None

    def valid_day(self, day):
        if day and day.isdigit():
            day = int(day)
            if day > 0 and day < 32:
                return day
        return None

    def valid_year(self, year):
        if year and year.isdigit():
            year = int(year)
            if year > 1900 and year < 2020:
                return year
        return None

class ThanksHandler(BaseHandler):
    def get(self):
        self.render('Templates/thanks.html')