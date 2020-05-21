#!/usr/bin/env python
# -*- coding: utf-8 -*-


# http://api.ipify.org/?format=json

import json

from fastapi import FastAPI

import deepnlpf._version as version
from deepnlpf.core.plugin_manager import PluginManager
from deepnlpf.models.mongodb import DataBase
from deepnlpf.pipeline import Pipeline
from deepnlpf.util.encoder import JSONEncoder

app = FastAPI()


@app.get("/")
async def root():
    return {
        "DeepNLPF": "Welcome API RESTFul",
        "Version": version.__version__,
        "Docs": "http://127.0.0.1:8000/docs",  # http://127.0.0.1:8000/docs
        "ReDoc": "http://127.0.0.1:8000/redoc",  # http://127.0.0.1:8000/redoc
    }


@app.get("/plugins")
async def plugins():
    return {"plugins": PluginManager().load_manifest()}


@app.get("/datasets")
async def datasets():
    response = {"datasets": DataBase().select_all()}
    response = JSONEncoder().encode(response)  # remove ObjectId
    response = json.loads(response)
    return response


@app.get("/processing")
async def processing(
    _input: str,
    pipeline: str,
    _output: str="terminal",
    _format: str="json",
    use_db: str=None,
    tool_base: str="stanza",
    boost: str="ray",
    memory: int=None,
    cpus: int=None,
    gpus: int=None,
):
    try:
        nlp = Pipeline(
            _input=_input,
            pipeline=pipeline,
            _output=_output,
            _format=_format,
            use_db=use_db,
            tool_base=tool_base,
            boost=boost,
            memory=memory,
            cpus=cpus,
            gpus=gpus,
        )

        results = nlp.annotate()

        return results
    except Exception as err:
        return err


@app.post("/processing")
def processing():
    tools_name = set()
    tools = []
    id_dataset = ""
    raw_text = ""

    # get json-form.
    response = request.get_json()

    # get tools_name in json-form.
    for index, item in enumerate(response):
        if index == 0:
            if item["name"] == "id_dataset":
                id_dataset = item["value"]
            elif item["name"] == "raw_text":
                raw_text = item["value"]

        if index > 0:
            tool, analyze = item["name"].split("-")
            tools_name.add(tool)

    # get analyse in json-form.
    for tool in tools_name:
        analyze = {"pipeline": []}

        for index, item in enumerate(response):
            # remove corpus.
            if index > 0:
                t, a = item["name"].split("-")
                if tool == t:
                    analyze["pipeline"].append(a)

    # config properties.
    item = {tool: analyze}
    tools.append(item)

    if id_dataset != "":
        conv = {"id_dateset": id_dataset, "tools": tools}
    elif raw_text != "":
        conv = {"raw_text": raw_text, "tools": tools}

    jsondata = json.dumps(conv)
    print(jsondata)

    # split
    raw_text = conv["raw_text"]
    pipeline = conv["tools"]
    output_format = ""

    # raw_text = jsondata['raw_text']
    # pipeline = jsondata['pipeline']

    # if jsondata['output_format'] != None:
    #    output_format = jsondata['output_format']
    try:
        print(pipeline)
        nlp = Pipeline(
            raw_text=raw_text, json_string=pipeline, output_format=output_format
        )
        return jsonify(nlp.annotate())
    except Exception as err:
        return err
