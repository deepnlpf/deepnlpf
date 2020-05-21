#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Credits: https://github.com/mxr/random-object-id

import binascii
import os
import time

from bson.objectid import ObjectId


class RandomObjectId(object):

    def gen_random_object_id_string(self):
        timestamp = '{0:x}'.format(int(time.time()))
        rest = binascii.b2a_hex(os.urandom(8)).decode('ascii')
        object_id = timestamp + rest
        
        return object_id

    def gen_random_object_id(self):
        timestamp = '{0:x}'.format(int(time.time()))
        rest = binascii.b2a_hex(os.urandom(8)).decode('ascii')
        object_id = timestamp + rest
        return ObjectId(object_id)
