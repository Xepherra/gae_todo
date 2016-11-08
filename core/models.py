from google.appengine.ext import ndb

#Used to retrieve an entity's Id
#This is used with the custom JSON serializer to send POJOs to a client
class ModelUtils(object):
    def to_dict(self):
        result = super(ModelUtils,self).to_dict()
        result['id'] = self.key.id() #get the key as a string
        return result

class ToDoItem(ModelUtils,ndb.Model):
    text = ndb.StringProperty(indexed = False)
    order = ndb.IntegerProperty(indexed = True)

class ToDo(ModelUtils,ndb.Model):
    title = ndb.StringProperty(indexed = True)
    create_date = ndb.DateTimeProperty(auto_now_add = True,indexed = True)
    items = ndb.StructuredProperty(ToDoItem,repeated = True)
