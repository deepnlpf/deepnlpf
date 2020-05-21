#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

import deepnlpf.log as log


class Util(object):
    def __init__(self):
        pass

    def openfile_json(self, path_file):
        try:
            with open(path_file, "r") as data:
                return json.load(data)
        except Exception as err:
            log.logger.error("Error loading file!" + str(err))

    def open_txt(self, path_file):
        data_temp = []

        try:
            with open(path_file) as data:
                for line in data:
                    data_temp.append(line.strip())
                return data_temp
        except Exception as err:
            log.logger.error("Error loading file!" + str(err))

    def save_txt(self, path_file, corpus):
        try:
            temp_file = open(path_file, "w")

            for line in corpus:
                temp_file.write(line + "\n")

            temp_file.close()
        except Exception as err:
            log.logger.error("Error loading file!" + str(err))

    def save_json(self, path_file, dataset):
        try:
            temp_file = open(path_file, "w")

            for line in dataset:
                temp_file.write(line + "\n")

            temp_file.close()
        except Exception as err:
            log.logger.error("Error loading file!" + str(err))

    def save_file(self, path_file_output, data):
        try:
            with open(path_file_output, "w") as file:
                file.write(data)
        except Exception as err:
            log.logger.error("Error loading file!" + str(err))

    def open_log(self, path_file):
        try:
            with open(path_file) as file:
                return file.read()
        except Exception as err:
            log.logger.error("Error loading file!" + str(err))
