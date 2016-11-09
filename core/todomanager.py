#Manages CRUD operations for the ToDo Entity
from core.models import *
from core.helper import *

def create_ToDo(todo_json):
    new_todo = ToDo()
    new_todo.title = todo_json['title']

    order = 1
    for td_jitem in todo_json['items']:
        new_tditem = ToDoItem()
        new_tditem.text = td_jitem['text']
        new_tditem.order = int(td_jitem['order']) if ('order' in td_jitem and td_jitem['order'] is not None) else order

        new_todo.items.append(new_tditem)
        order +=1

    new_todo.put()
    return new_todo

def get_ToDos():
    return ToDo.query().fetch()

def get_ToDo(todo_id):
    return ToDo.get_by_id(long(todo_id))

def update_ToDo(todo_id,todo_json):
    todo_record = ToDo.get_by_id(long(todo_id))
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
    return todo_record

def delete_ToDo(todo_id):
    todo_record = ToDo.get_by_id(long(todo_id))
    if todo_record is not None:
        todo_record.key.delete()
        return True
    else:
        return False
