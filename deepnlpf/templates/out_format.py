# -*- coding: utf-8 -*-
"""[summary]

Returns:
    [type] -- [description]
"""

import datetime


class OutFormat(object):

    def __init__(self):
        pass

    def doc_annotation(self, _id_pool, _id_dataset, _id_document, tool, annotation):
        return {
            "_id_pool": _id_pool,
            "_id_dataset": _id_dataset,
            "_id_document": _id_document,
            "tool": tool,
            "annotation": annotation,
            "last_modified": datetime.datetime.now()
        }
