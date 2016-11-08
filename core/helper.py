from datetime import datetime

import json

class CustomJsonEncoder(json.JSONEncoder):
   def default(self, obj):
      if isinstance(obj, datetime):
         # format however you like/need
         return obj.strftime("%Y-%m-%d")
      # pass any other unknown types to the base class handler, probably
      # to raise a TypeError.
      return json.JSONEncoder.default(self, obj)
