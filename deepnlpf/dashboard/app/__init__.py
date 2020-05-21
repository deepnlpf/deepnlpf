#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import os
import pandas as pd
import plotly
import plotly.graph_objs as go
import requests
import zipfile
from flask import Flask, flash, redirect
from flask import render_template, request, jsonify, Response
from plotly.graph_objs import *
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = set(['zip'])

app = Flask(__name__, instance_relative_config=True)

app.secret_key = "JebwpwqaiXdmqteOmjUxpJdVufWJyneL"
app.config['UPLOAD_FOLDER'] = os.environ['HOME'] + '/datasets/uploads'
# app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

# Load the views


server = ''


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/upload_file', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)

        file = request.files['file']

        if file.filename == '':
            flash('No file selected for uploading')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            path_dataset = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(path_dataset)

            fantasy_zip = zipfile.ZipFile(path_dataset)
            fantasy_zip.extractall(app.config['UPLOAD_FOLDER'])
            os.remove(path_dataset)
            fantasy_zip.close()
            
            conv = {'path_corpus': str(os.path.splitext(path_dataset)[0])}
            s = json.dumps(conv)
            requests.post(server+"/corpus_upload", json=s).json()
            
            flash('File successfully uploaded')
            return redirect('/')
        else:
            flash('Allowed file types are zip')
            return redirect(request.url)


@app.route('/', methods=["GET", "POST"])
def annotation():
    if request.method == 'POST':
        option_selected = {}
        data = request.form['form-options']

        # step 1
        option_selected['dataset'] = request.form.get('name_dataset')

    conv = [{'input': 'hi', 'topic': 'Greeting'}]
    s = json.dumps(conv)
    response = requests.post(server+"/annotation", json=s).json()

    return render_template(
        "annotation.html",
        page="DeepNLPF DashBoard >> Annotation",
        corpus=response['corpus'],
        plugins=response['plugins']
    )


@app.route('/annotation_processing', methods=["GET", "POST"])
def annotation_processing():
    if request.method == 'POST':
        response = request.get_json()

        # properties = {'tools': []}
        tools_name = set()
        tools = []
        id_corpus = ''

        # get tools_name.
        for index, item in enumerate(response['options']):
            if index == 0:
                id_corpus = item['value']

            if index > 0:
                tool, analyze = item['name'].split('-')
                tools_name.add(tool)

        # get analyse.
        for tool in tools_name:
            analyze = {'pipeline': []}
            for index, item in enumerate(response['options']):
                # remove corpus.
                if index > 0:
                    t, a = item['name'].split('-')
                    if(tool == t):
                        analyze['pipeline'].append(a)

            # config properties.
            item = {tool: analyze}
            # properties['tools'].append(item)
            tools.append(item)

        # conv = {'id_corpus': id_corpus, 'properties': properties}
        conv = {'id_corpus': id_corpus, 'tools': tools}
        s = json.dumps(conv)

        res = requests.post(server+"/annotation_processing", json=s).json()

    return jsonify(response)


@app.route('/corpus')
def Dataset():
    conv = [{'input': 'hi', 'topic': 'Greeting'}]
    s = json.dumps(conv)
    response = requests.post(server+"/corpus", json=s).json()
    return render_template("corpus.html", corpus=response['corpus'])


@app.route('/corpus_view', methods=['GET'])
def corpus_view():
    conv = {'_id': request.args.get('_id')}
    s = json.dumps(conv)
    response = requests.post(server+"/corpus_view", json=s).json()

    return render_template(
        "corpus_view.html",
        page="DeepNLPF DashBoard >> View Corpus",
        corpus=response['corpus'],
        documents=response['documents']
    )


@app.route('/corpus_statistic', methods=['GET'])
def corpus_statistic():
    conv = {'_id': request.args.get('_id')}
    s = json.dumps(conv)
    response = requests.post(server+"/corpus_statistic", json=s).json()

    if(response):
        feature = 'word_cloud'  # FreqWords, Bar, Scatter, WordCloud

        wordcloud = create_plot('word_cloud', response['statistics'])
        bar = create_plot('token_frequency_by_class_grammtical',
                          response['statistics'])
        bar_2 = create_plot('token_frequency_by_sentences',
                            response['statistics'])

        return render_template("corpus_statistic.html",
                               page="DeepNLPF DashBoard >> Corpus Statistic",
                               corpus=response['corpus'],
                               statistics=response['statistics'],
                               bar=bar, bar_2=bar_2,
                               wordcloud=wordcloud
                               )


def create_plot(feature, dt):
    x = []
    y = []

    for item in dt['words_frequency']:
        x.append(item['freq'])
        y.append(item['word'])

    if feature == 'Bar':
        df = pd.DataFrame({'x': x, 'y': y})  # creating a sample dataframe
        data = [
            go.Bar(
                x=df['x'],  # assign x as the dataframe column 'x'
                y=df['y']
            )
        ]
    elif feature == 'FreqWords':
        trace = {
            "x": x,
            "y": y,
            "marker": {"color": "rgb(84, 172, 234)"},
            "orientation": "h",
            "type": "bar"
        }
        data = Data([trace])

    elif feature == 'token_frequency_by_class_grammtical':
        fig = go.Figure()

        for item in dt['post_tag_frequency']:
            cont = []

            for _ in range(int(item['freq'])):
                cont.append(item['pos'])

            fig.add_trace(go.Histogram(x=cont, name=item['pos']))

        fig.update_layout(
            # title_text='Frequency of Tokens to Grammatical Class',
            xaxis_title_text='Grammatical Class',
            yaxis_title_text='Words Frequency',
            bargap=0.2,
            bargroupgap=0.1,
            showlegend=True
        )

        data = fig

    elif feature == 'token_frequency_by_sentences':
        fig = go.Figure(
            data=[go.Histogram(x=dt['tokens_frequency_to_sentences'])]
        )

        fig.update_layout(
            xaxis_title_text='Number Tokens',
            yaxis_title_text='Sentences Frequency',
            bargap=0.2,
            bargroupgap=0.1
        )

        data = fig

    elif feature == 'word_cloud':
        import random

        words = y
        size = 30

        colors = [plotly.colors.DEFAULT_PLOTLY_COLORS[random.randrange(
            1, 10)] for i in range(size)]
        weights = [random.randint(15, 35) for i in range(size)]

        data = go.Scatter(
            x=[random.random() for i in range(size)],
            y=random.choices(range(30), k=30),
            mode='text',
            text=words,
            marker={'opacity': 0.3},
            textfont={'size': weights, 'color': colors}
        )

        layout = go.Layout({
            'xaxis': {'showgrid': False, 'showticklabels': False, 'zeroline': False},
            'yaxis': {'showgrid': False, 'showticklabels': False, 'zeroline': False}
        })

        data = go.Figure(data=[data], layout=layout)

    else:
        # Create a trace
        data = [go.Scatter(
            x=x,
            y=y,
            mode='markers'
        )]

    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON


@app.route('/bar', methods=['GET', 'POST'])
def change_features():
    feature = request.args['selected']
    graphJSON = self.create_plot(feature)
    return graphJSON


@app.route('/corpus_analysis', methods=['GET'])
def corpus_analysis():
    page = "DeepNLPF DashBoard >> Corpus Analysis Tools"

    conv = {'_id': request.args.get('_id')}
    s = json.dumps(conv)
    response = requests.post(server+"/corpus_analysis", json=s).json()

    return render_template(
        "corpus_analysis.html",
        page=page,
        corpus=response['corpus'],
        annotations=response['annotations']
    )


@app.route('/corpus_upload', methods=['GET', 'POST'])
def corpus_upload():
    headers = {'accept': 'application/json'}
    conv = {'path_corpus': request.args.get('path_corpus')}
    s = json.dumps(conv)
    response = requests.post(server+"/corpus_upload",
                             headers=headers, json=s).json()
    return jsonify(response)


@app.route('/corpus_download', methods=['GET'])
def corpus_download():
    headers = {'accept': 'application/json'}
    conv = {'_id': request.args.get('_id')}
    s = json.dumps(conv)
    response = requests.post(server+"/corpus_download",
                             headers=headers, json=s).json()

    generator = (cell for row in response['sentences'] for cell in row+"\n")

    file_name = response['name']

    return Response(
        generator,
        mimetype="text/txt",
        headers={"Content-Disposition": "attachment; filename="+file_name+".txt"}
    )


@app.route('/corpus_delete', methods=['GET'])
def corpus_delete():
    headers = {'accept': 'application/json'}
    conv = {'_id': request.args.get('_id')}
    s = json.dumps(conv)
    response = requests.post(server+"/corpus_delete",
                             headers=headers, json=s).json()
    return jsonify(response)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/configurations')
def configurations():
    return render_template("configurations.html")


# Load the config file
# app.config.from_object('config')
app.config['DEBUG'] = True
app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
