#!/usr/bin/env python
# -*- coding: utf-8 -*-


#http://api.ipify.org/?format=json

import json

import deepnlpf._version as version

from deepnlpf.pipeline import Pipeline
from deepnlpf.models.mongodb import DataBase
from deepnlpf.util.encoder import JSONEncoder
from deepnlpf.core.plugin_manager import PluginManager

from fastapi import FastAPI

app = FastAPI()



@app.get("/")
def read_root():
    return {
        "DeepNLPF": "Welcome API RESTFul",
        "Version": version.__version__,
        "Docs": "http://127.0.0.1:8000/docs", # http://127.0.0.1:8000/docs
        "ReDoc": "http://127.0.0.1:8000/redoc" # http://127.0.0.1:8000/redoc
        }



@app.get("/plugins")
def plugins():
    return {'plugins': PluginManager().load_manifest()}



@app.get('/datasets')
def datasets():
    response = {'datasets': DataBase().select_all()}
    response = JSONEncoder().encode(response) # remove ObjectId
    response = json.loads(response)
    return response



@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}