#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from flask import Flask, jsonify, request

from deepnlpf.pipeline import Pipeline

from deepnlpf.models.mongodb import DataBase

from deepnlpf.core.encoder import JSONEncoder
from deepnlpf.core.plugin_manager import PluginManager

app = Flask(__name__, instance_relative_config=True)

app.config['DEBUG'] = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SECRET_KEY'] = 'JebwpwqaiXdmqteOmjUxpJdVufWJyneL'

app.jinja_env.auto_reload = True

@app.route('/')
def index():
    return jsonify({
        "DeepNLPF": "Welcome API REST",
        "Version": "1.0.11"
        })
        
@app.route('/monitor')
def monitor():
    # User / IP (http://api.ipify.org/?format=json)
    # CPU
    # RAM
    # Swap
    # Disk
    # GPU
    # Network
    # Profiling
    pass

@app.after_request
def add_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    return response


@app.route('/get_all_plugins', methods=['POST', 'GET'])
def get_all_plugins():
    if request.method == 'POST':
        response = {'plugins': PluginManager().load_plugin_manifest()}
        return jsonify(response)

@app.route('/get_all_datasets', methods=['POST', 'GET'])
def get_all_dataset():
    if request.method == 'POST':
        response = {'datasets': DataBase().select_all()}
        response = JSONEncoder().encode(response) # remove ObjectId
        response = json.loads(response)
        return jsonify(response)

@app.route('/processing', methods=['POST', 'GET'])
def processing():
    if request.method == 'POST':
        response = request.get_json()
        jsondata = json.loads(response)

        raw_text = jsondata['raw_text']
        pipeline = jsondata['pipeline']
        
        if jsondata['output_format'] != None:
            output_format = jsondata['output_format']
            
    else:#GET
        #_id_dataset = request.args.get('_id_dataset')
        raw_text = request.args.get('raw_text')
        pipeline = request.args.get('pipeline')
        output_format = request.args.get('output_format')
    
    try:
        print(">>> OK!")
        nlp = Pipeline(raw_text=raw_text, json_string=pipeline, output_format=output_format)
        return jsonify(nlp.annotate())
    except Exception as err:
        return err

"""
     Estátisticas 

     1. stop-word chart 
     2. non-stop word chart 
     3. top - ngram  (100) 
     4. POS chart 
     5. NER (most common and Bar chart)
"""

if __name__ == "__main__":
    app.run(debug=True)