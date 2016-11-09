# [START imports]
import os
import urllib
import json

import jinja2
import webapp2

from core.models import *
from core.helper import *

import core.todomanager as tdm

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
# [END imports]

# [START main_page]
class App(webapp2.RequestHandler):
    def get(self):
        template_values = {'message' : 'Hello this is a header'}
        template = JINJA_ENVIRONMENT.get_template('templates/index.html')
        self.response.write(template.render(template_values))
# [END main_page]

# [START ToDos API handler]
class ToDosAPI(webapp2.RequestHandler):
    def get(self):
        json_response = json.dumps([td.to_dict() for td in tdm.get_ToDos()],cls=CustomJsonEncoder)
        self.response.headers['Content-Type'] = "application/json"
        self.response.write(json_response)

    def post(self):
        payload = json.loads(self.request.body)
        self.response.headers['Content-Type'] = "application/json"
        self.response.write(json.dumps(tdm.create_ToDo(payload).to_dict(),cls=CustomJsonEncoder))
# [END API handler]

# [START ToDo API handler]
class ToDoAPI(webapp2.RequestHandler):
    def get(self,todo_id):
        todo = tdm.get_ToDo(todo_id)
        if todo is None:
            self.error(404)
        else:
            self.response.headers['Content-Type'] = "application/json"
            self.response.write(json.dumps(todo.to_dict(),cls=CustomJsonEncoder))

    def put(self,todo_id):
        todo_json = json.loads(self.request.body)
        self.response.headers['Content-Type'] = "application/json"
        self.response.write(json.dumps(tdm.update_ToDo(todo_id,todo_json).to_dict(),cls=CustomJsonEncoder))

    def delete(self,todo_id):
        if not tdm.delete_ToDo(todo_id):
            self.error(404)
# [End ToDo API handler]

# [START app]
app = webapp2.WSGIApplication([
    ('/', App),
    ('/api/todos',ToDosAPI),
    ('/api/todo/(\w+)',ToDoAPI)
], debug=True)
# [END app]
