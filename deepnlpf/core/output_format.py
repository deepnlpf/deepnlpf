# -*- coding: utf-8 -*-

import json
from datetime import datetime

from json2xml import json2xml


class OutputFormat:

    def __init__(self):
        pass

    def data_time(self):
        return json.dumps(datetime.now().strftime('%d/%m/%Y - %H:%M:%S'))

    def doc_annotation(self, _id_pool, _id_dataset, _id_document, tool, annotation):
        return {
            "_id_pool": _id_pool,
            "_id_dataset": _id_dataset,
            "_id_document": _id_document,
            "tool": tool,
            "annotation": annotation,
            "data_time": self.data_time()
        }

    def json2xml(self, json_data):
        return json2xml.Json2xml(json_data, wrapper="all", pretty=True).to_xml()

    def xml2json(self, xml_file):
        import xmltodict

        with open(xml_file) as file:
            doc = xmltodict.parse(file.read())
        return json.dumps(doc)

    def yaml2json(self, yaml_file):
        import yaml

        with open(yaml_file) as file:
            doc = json.dumps(yaml.safe_load(file))

        return json.loads(doc)



class ValidatingJSON(object):
    # https://github.com/Julian/jsonschema

    def __init__(self):
       pass



# tests
if __name__ == "__main__":
    json_data = {'tool': 'semaifor', 'dataset': 'test1', 'sentences': [{'frames': [{'target': {'name': 'Substance', 'spans': [{'start': 2, 'end': 3, 'text': 'juice'}]}, 'annotationSets': [{'rank': 0, 'score': 25.388448698934354, 'frameElements': [{'name': 'Substance', 'spans': [{'start': 2, 'end': 3, 'text': 'juice'}]}]}]}, {'target': {'name': 'Degree', 'spans': [{'start': 4, 'end': 5, 'text': 'very'}]}, 'annotationSets': [{'rank': 0, 'score': 3.602812903981236, 'frameElements': [{'name': 'Gradable_attribute', 'spans': [{'start': 5, 'end': 6, 'text': 'savory'}]}]}]}, {'target': {'name': 'Chemical-sense_description', 'spans': [{'start': 5, 'end': 6, 'text': 'savory'}]}, 'annotationSets': [{'rank': 0, 'score': 9.733314310523166, 'frameElements': []}]}], 'tokens': ['This', 'mango', 'juice', 'is', 'very', 'savory', '.']}, {'frames': [{'target': {'name': 'Desiring', 'spans': [{'start': 1, 'end': 2, 'text': 'want'}]}, 'annotationSets': [{'rank': 0, 'score': 78.66847857754101, 'frameElements': [{'name': 'Experiencer', 'spans': [{'start': 0, 'end': 1, 'text': 'I'}]}, {'name': 'Event', 'spans': [{'start': 2, 'end': 7, 'text': 'to play with the horse'}]}]}]}, {'target': {'name': 'Performers_and_roles', 'spans': [{'start': 3, 'end': 4, 'text': 'play'}]}, 'annotationSets': [{'rank': 0, 'score': 42.4740879307544, 'frameElements': [{'name': 'Performance', 'spans': [{'start': 4, 'end': 7, 'text': 'with the horse'}]}]}]}], 'tokens': ['I', 'want', 'to', 'play', 'with', 'the', 'horse', '.']}, {'frames': [{'target': {'name': 'Substance', 'spans': [{'start': 2, 'end': 3, 'text': 'juice'}]}, 'annotationSets': [{'rank': 0, 'score': 25.388448698934354, 'frameElements': [{'name': 'Substance', 'spans': [{'start': 2, 'end': 3, 'text': 'juice'}]}]}]}, {'target': {'name': 'Degree', 'spans': [{'start': 4, 'end': 5, 'text': 'very'}]}, 'annotationSets': [{'rank': 0, 'score': 3.602812903981236, 'frameElements': [{'name': 'Gradable_attribute', 'spans': [{'start': 5, 'end': 6, 'text': 'savory'}]}]}]}, {'target': {'name': 'Chemical-sense_description', 'spans': [{'start': 5, 'end': 6, 'text': 'savory'}]}, 'annotationSets': [{'rank': 0, 'score': 9.733314310523166, 'frameElements': []}]}], 'tokens': ['This', 'mango', 'juice', 'is', 'very', 'savory', '.']}, {'frames': [{'target': {'name': 'Calendric_unit', 'spans': [{'start': 0, 'end': 1, 'text': 'Today'}]}, 'annotationSets': [{'rank': 0, 'score': 28.292225395221365, 'frameElements': [{'name': 'Unit', 'spans': [{'start': 0, 'end': 1, 'text': 'Today'}]}]}]}, {'target': {'name': 'Calendric_unit', 'spans': [{'start': 3, 'end': 4, 'text': 'day'}]}, 'annotationSets': [{'rank': 0, 'score': 26.08802997724397, 'frameElements': [{'name': 'Unit', 'spans': [{'start': 3, 'end': 4, 'text': 'day'}]}]}]}], 'tokens': ['Today', '10/25/2018', 'the', 'day', 'is', 'cloudy', '.']}, {'frames': [{'target': {'name': 'Ingestion', 'spans': [{'start': 1, 'end': 2, 'text': 'drank'}]}, 'annotationSets': [{'rank': 0, 'score': 34.42346833051987, 'frameElements': []}]}, {'target': {'name': 'Finish_competition', 'spans': [{'start': 5, 'end': 6, 'text': 'Victor'}]}, 'annotationSets': [{'rank': 0, 'score': 47.58351955145408, 'frameElements': []}]}, {'target': {'name': 'Causation', 'spans': [{'start': 7, 'end': 8, 'text': 'caused'}]}, 'annotationSets': [{'rank': 0, 'score': 64.43905312888936, 'frameElements': [{'name': 'Effect', 'spans': [{'start': 8, 'end': 11, 'text': 'the greatest confusion'}]}]}]}, {'target': {'name': 'Desirability', 'spans': [{'start': 9, 'end': 10, 'text': 'greatest'}]}, 'annotationSets': [{'rank': 0, 'score': 29.774720873859444, 'frameElements': [{'name': 'Evaluee', 'spans': [{'start': 10, 'end': 11, 'text': 'confusion'}]}]}]}], 'tokens': ['Camila', 'drank', 'the', 'soda', 'from', 'Victor', 'and', 'caused', 'the', 'greatest', 'confusion', '.']}]}
    print(OutputFormat().json2xml(json_data))