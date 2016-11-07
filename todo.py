# [START imports]
import os
import urllib

import jinja2
import webapp2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
# [END imports]


# [START main_page]
class ToDo(webapp2.RequestHandler):
    def get(self):
        self.response.write("Hello ToDo")
# [END main_page]

# [START app]
app = webapp2.WSGIApplication([
    ('/', ToDo)
], debug=True)
# [END app]
