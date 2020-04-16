#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Date: 07/03/2019
"""

import os, json, datetime

class Util(object):

    def __init__(self):
        pass

    def openfile_json(self, path_file):
        try:
            with open(path_file, 'r') as file:
                return json.load(file)
        except Exception as err:
            return "Error loading file!" + err

    def open_txt(self, path_file):
        data_temp = []
        
        try:
            with open(path_file) as file:
                for line in file:
                    data_temp.append(line.strip())
                return data_temp
        except Exception as err:
            return "Error loading file!" + str(err)

    def save_txt(self, path_file, corpus):
        try:
            temp_file = open(path_file, 'w')
        
            for line in corpus:
                temp_file.write(line+"\n")

            temp_file.close()
        except Exception as err:
            print(err)

    def save_json(self, path_file, corpus):
        try:
            temp_file = open(path_file, 'w')
        
            for line in corpus:
                temp_file.write(line+"\n")

            temp_file.close()
        except Exception as err:
            print(err)

    def save_file(self, path_file_output, data):
        try:
            with open(path_file_output, 'w') as file:
                file.write(data)
        except Exception as err:
            print(err)