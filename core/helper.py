from datetime import datetime

import json

'''
This is a custom JSON encoder which allows for Date serialization
ndb models used by GAE cannot serialize Date properties using the to_dict method
this class takes care of that
'''
class CustomJsonEncoder(json.JSONEncoder):
   def default(self, obj):
      if isinstance(obj, datetime):
         # format however you like/need
         return obj.strftime("%Y-%m-%d")
      # pass any other unknown types to the base class handler, probably
      # to raise a TypeError.
      return json.JSONEncoder.default(self, obj)
