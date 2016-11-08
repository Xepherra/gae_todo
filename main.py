# [START imports]
import os
import urllib
import json

import jinja2
import webapp2

from core.models import *
from core.helper import *

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
        json_response = json.dumps([td.to_dict() for td in ToDo.query().fetch()],cls=CustomJsonEncoder)
        self.response.headers['Content-Type'] = "application/json"
        self.response.write(json_response)

    def post(self):
        payload = json.loads(self.request.body)
        new_todo = ToDo()
        new_todo.title = payload['title']
        new_todo.put()
        self.response.write(self.request.body)

# [END API handler]

# [START app]
app = webapp2.WSGIApplication([
    ('/', App),
    ('/api/todo',ToDoAPI)
], debug=True)
# [END app]
