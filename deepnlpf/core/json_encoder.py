""" JSONEncoder
    Remove ObjectId of json.
"""

import json
from bson import ObjectId

class JSONEncoder(json.JSONEncoder):

    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)