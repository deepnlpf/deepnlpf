<div align="center"><img src="https://github.com/deepnlpf/deepnlpf/blob/master/images/deepnlpf-logo.png" height="100px"/></div>

<h2 align="center">DeepNLPF: A Framework for Integrating Linguistic Analysis and Semantic Annotation of Text Documents.</h2>

<div align="center">
    <a href="#">
        <img alt="License" src="https://img.shields.io/github/license/deepnlpf/deepnlpf">
    </a>
    <a href="https://pypi.org/project/deepnlpframework/">
        <img alt="PyPI Version" src="https://img.shields.io/pypi/v/deepnlpframework?color=blue">
    </a>
    <a href="https://anaconda.org/deepnlpframework">
        <img alt="Conda Versions" src="https://img.shields.io/conda/vn/deepnlpframework?color=blue&label=conda">
    </a>
    <a href="https://pypi.org/project/deepnlpframework/">
        <img alt="Python Versions" src="https://img.shields.io/pypi/pyversions/deepnlpframework?colorB=blue">
    </a>
</div>

The DeepNLPF it contains support for running various accurate natural language processing tools. For detailed information please visit our [official website](https://deepnlpf.github.io/site).

DeepNLPF has been implemented and tested using the [Ubuntu](https://ubuntu.com/) 19.04 operating system. However, it may work on other similar linux versions or Windows and MacOS if it satisfies the dependencies on external NLP tools mentioned below "at your own risk".

## System requirements
<b>Hardware</b>
* Memoria RAM: Min. 16GB.
* CPU Core: Min. Dualcore
* Disk Space: ~ MB (does not include disk space for IDE/tools).

<b>Software</b>
* [Download Ubuntu 19.04](https://ubuntu.com/) (64-bit).
* [Intall Python 3.7](https://linuxize.com/post/how-to-install-python-3-7-on-ubuntu-18-04/) 
* [Install Java 8](https://tecadmin.net/install-oracle-java-8-ubuntu-via-ppa/)
* [Intall MongoDB](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/)

## [Pip](https://pypi.org/project/pip/) install

        $ pip install deepnlpframework
        
        $ deepnlpf --install stanfordcorenlp #install plugin base stanford corenlp.

## Getting Started

To see DeepnlpF custom pipeline in action, you can launch the Python interactive interpreter, and try the following commands:

    >>> from deepnlpf.pipeline import Pipeline
    >>> custom_pipeline = """
        {
            "tools": [{
                "stanfordcorenlp": {
                    "pipeline": [
                        "tokenize",
                        "ssplit",
                        "pos",
                        "lemma",
                        "ner",
                        "parse",
                        "depparse",
                        "truecase",
                        "dcoref"
                    ]
                }
            }]
        }
        """

    >>> sentence = "Barack Obama was born in Hawaii."
    >>> nlp = Pipeline(raw_text=sentence, json_string=custom_pipeline)
    >>> nlp.annotate()

## LICENSE
DeepNLPF is released under the Apache License, Version 2.0. See the [LICENSE](https://github.com/deepnlpf/deepnlpf/blob/master/README.md) file for more details.