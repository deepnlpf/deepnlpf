# -*- coding: utf-8 -*-
"""
"""
class PreProcessing(object):
    """
    """

    def remove_special_characters(self, sentence):
        import re
        return re.sub(r'[-_./?,`":;=+()|@#$%&*^~\']', '', sentence)
