from google.appengine.ext import ndb

class ToDoItem(ndb.Model):
    text = ndb.StringProperty(indexed = False)
    order = ndb.IntegerProperty(indexed = True)

class ToDo(ndb.Model):
    title = ndb.StringProperty(indexed = True)
    create_date = ndb.DateTimeProperty(auto_now_add = True,indexed = True)
    items = ndb.StructuredProperty(ToDoItem,repeated = True)
