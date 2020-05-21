import os
from os import path

HOME = os.environ['HOME']
HERE = path.abspath(path.dirname(__file__))

FILE_CONFIG = HERE + "/config.ini"

INPUT_FORMAT_DATASET = [
    "path_dataset", 
    "id_dataset", 
    "raw_text"
]

INPUT_FORMAT_PIPELINE = [
    "json", 
    "json_str", 
    "json_url", 
    "yaml", 
    "yaml_str",
    "yaml_url", 
    "xml",
    "xml_str",
    "xml_url",
    "ini",
    "ini_str"
    "ini_url", 
]