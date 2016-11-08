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

# [START ToDos API handler]
class ToDosAPI(webapp2.RequestHandler):
    def get(self):
        json_response = json.dumps([td.to_dict() for td in ToDo.query().fetch()],cls=CustomJsonEncoder)
        self.response.headers['Content-Type'] = "application/json"
        self.response.write(json_response)

    def post(self):
        payload = json.loads(self.request.body)
        new_todo = ToDo()
        new_todo.title = payload['title']

        order = 1
        for td_jitem in payload['items']:
            new_tditem = ToDoItem()
            new_tditem.text = td_jitem['text']
            new_tditem.order = int(td_jitem['order']) if ('order' in td_jitem and td_jitem['order'] is not None) else order

            new_todo.items.append(new_tditem)
            order +=1

        new_todo.put()
        self.response.write(self.request.body)
# [END API handler]

# [START ToDo API handler]
class ToDoAPI(webapp2.RequestHandler):
    def get(self,todo_id):
        todo = ToDo.get_by_id(long(todo_id))
        if todo is None:
            self.error(404)
        else:
            self.response.headers['Content-Type'] = "application/json"
            self.response.write(json.dumps(todo.to_dict(),cls=CustomJsonEncoder))
    def put(self,todo_id):
        todo_json = json.loads(self.request.body)
        todo_record = ToDo.get_by_id(long(todo_json['id']))
        todo_record.title = todo_json['title']

        #clear the list
        del todo_record.items[:]

        order = 1
        for td_jitem in todo_json['items']:
            #handle items here
            td_item = ToDoItem()
            td_item.order = int(td_jitem['order']) if ('order' in td_jitem and td_jitem['order'] is not None) else order
            td_item.text = td_jitem['text']
            todo_record.items.append(td_item)
            order +=1

        todo_record.put()

    def delete(self,todo_id):
        todo_record = ToDo.get_by_id(long(todo_id))
        if todo_record is not None:
            todo_record.key.delete()
        else:
            self.error(404)

# [End ToDo API handler]

# [START app]
app = webapp2.WSGIApplication([
    ('/', App),
    ('/api/todos',ToDosAPI),
    ('/api/todo/(\w+)',ToDoAPI)
], debug=True)
# [END app]
