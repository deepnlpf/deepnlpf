from flask import Flask, jsonify, request

from deepnlpf.pipeline import Pipeline

app = Flask(__name__, instance_relative_config=True)

app.config['DEBUG'] = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SECRET_KEY'] = 'JebwpwqaiXdmqteOmjUxpJdVufWJyneL'

app.jinja_env.auto_reload = True

@app.route('/')
def index():
    return jsonify({'DeepNLPF': 'Hello API REST!'})

@app.route('/processing_dataset', methods=['POST', 'GET'])
def processing_dataset():
    #_id_dataset = request.args.get('_id_dataset')
    raw_text = request.args.get('raw_text')
    pipeline = request.args.get('pipeline')

    nlp = Pipeline(raw_text=raw_text, json_string=pipeline)
    annotation = nlp.annotate()
    return jsonify(annotation)

if __name__ == "__main__":
    app.run(debug=True)