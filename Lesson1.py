import webapp2

form = """

<form method = "post"> 
    <br>
    What is your birthday?
    <br>
    <br>
    <label>
        Month
        <input type = "text" name = "month" value = "%(month)s">
    </label>
    <label>
        Day
        <input type = "text" name = "day" value = "%(day)s">
    </label>
    <label>
        Year
        <input type = "text" name = "year" value = "%(year)s">
    </label>
    <div style = "color: red">%(error)s</div>
    <br>
    <br>
    <input type = "submit">

</form>
"""

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

def valid_month(month):
    if month and month.capitalize() in months:
        return month.capitalize()
    return None

def valid_day(day):
    if day and day.isdigit():
        day = int(day)
        if day > 0 and day < 32:
            return day
    return None

def valid_year(year):
    if year and year.isdigit():
        year = int(year)
        if year > 1900 and year < 2020:
            return year
    return None

import cgi
def escape_html(s):
    return cgi.escape(s, quote = True)

class MainPage(webapp2.RequestHandler):

    def write_form(self, error="", month="", day="", year=""):
        self.response.out.write(form % {"error" : escape_html(error),
                                        "month" : escape_html(month),
                                        "day" : escape_html(day),
                                        "year" : escape_html(year)})
    import cgi
    def escape_html(self, s):
        return cgi.escape(s, quote = True)

    def get(self):
        """self.response.headers['Content-Type'] = 'text/plain'"""
        self.response.write('Hello, Udacity! I cant believe I spent so much time trying to install this shit ' +
            'and this is all I know how to do at the moment!')
        self.write_form()

    def post(self):
        user_month = self.request.get('month')
        user_day = self.request.get('day')
        user_year = self.request.get('year')

        month = valid_month(user_month)
        day = valid_day(user_day)
        year = valid_year(user_year)

        if not(month and day and year):
            self.write_form("incorrect date", user_month, user_day, user_year)
        else:
            self.redirect("/thanks")

class ThanksHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write("Thanks! That's a totally valid day!")

app = webapp2.WSGIApplication([('/', MainPage), ('/thanks', ThanksHandler)], 
    debug=True)