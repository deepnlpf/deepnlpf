#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from datetime import datetime

from bson import ObjectId


class DTEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return list(obj.timetuple())[0:6]
        return json.JSONEncoder.default(self, obj)

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)