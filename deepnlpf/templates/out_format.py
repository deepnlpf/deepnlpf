# -*- coding: utf-8 -*-
"""[summary]

Returns:
    [type] -- [description]
"""

class OutFormat(object):

    def __init__(self):
        pass

    def data_time(self):
        from datetime import datetime
        return datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def doc_annotation(self, _id_pool, _id_dataset, _id_document, tool, annotation):
        return {
            "_id_pool": _id_pool,
            "_id_dataset": _id_dataset,
            "_id_document": _id_document,
            "tool": tool,
            "annotation": annotation,
            "last_modified": self.data_time()
        }
