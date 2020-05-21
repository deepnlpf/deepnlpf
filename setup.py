#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from codecs import open
from os import path

from setuptools import find_packages, setup

import deepnlpf._version as v

HERE = path.abspath(path.dirname(__file__))
HOME = os.environ['HOME']

VERSION = v.__version__

def readme():
    with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
        README = f.read()
    return README

def requirements():
    with open(path.join(HERE, 'requirements.txt')) as fp:
        REQUIRED = fp.read().splitlines()
    return REQUIRED

setup(
    name="deepnlpf",
    version=VERSION,
    description="A Framework for Integrating Linguistic Analysis and Semantic Annotation of Text Documents.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://deepnlpf.github.io/site",
    author="RodriguesFAS",
    author_email="franciscosouzaacer@gmail.com",

    # What does your project relate to?
    keywords='natural-language-processing nlp natural-language-understanding deepnlp deep-learning',

    # Choose your license
    license="Apache License 2.0",

    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Information Technology',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Text Processing',
        'Topic :: Text Processing :: Linguistic',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',

        # Specify the Python versions you support HERE. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.7',
    ],

    packages=find_packages(
        exclude=(
            "docker",
            "images",
            "tests",
            "examples",
            "scripts"
        )
    ),

    include_package_data=True,
    
    package_data = {'deepnlpf': ['config.ini', 'data.log']},

    # Create dir.
    data_files=[
        (HOME+'/deepnlpf_data', []),
        (HOME+'/deepnlpf_data/plugins', []),
        (HOME+'/deepnlpf_data/output', [])
    ],


    install_requires=requirements(),

    python_requires='>=3',

    entry_points={
        "console_scripts": [
            "deepnlpf=deepnlpf.__main__:main"
        ]
    }

)
