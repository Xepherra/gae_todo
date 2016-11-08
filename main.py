# [START imports]
import os
import urllib

import jinja2
import webapp2

from core.models import *

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
# [END imports]


# [START main_page]
class App(webapp2.RequestHandler):
    def get(self):

        template_values = {
            'message' : 'Hello this is a header'
        }

        template = JINJA_ENVIRONMENT.get_template('templates/index.html')
        self.response.write(template.render(template_values))
# [END main_page]

# [START API handler]
class ToDoAPI(webapp2.RequestHandler):
    def get(self):
        self.response.write("Hello API")

# [END API handler]

# [START app]
app = webapp2.WSGIApplication([
    ('/', App),
    ('/api/todo',ToDoAPI)
], debug=True)
# [END app]
