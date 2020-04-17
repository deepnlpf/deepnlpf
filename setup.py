#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re

from os import path
from codecs import open
from setuptools import setup, Extension, find_packages

here = path.abspath(path.dirname(__file__))
HOME = os.environ['HOME']

# read the version from deepnlpf/_version.py
version_file_contents = open(
    path.join(here, 'deepnlpf/_version.py'), encoding='utf-8').read()
VERSION = re.compile(
    '__version__ = \"(.*)\"').search(version_file_contents).group(1)

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    README = f.read()

with open(path.join(here, 'requirements.txt')) as fp:
    REQUIRED = fp.read().splitlines()

# This call to setup() does all the work
setup(
    name="deepnlpf",
    version=VERSION,
    description="A Framework for Integrating Linguistic Analysis and Semantic Annotation of Text Documents.",
    long_description=README,
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

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.7',
    ],

    packages=find_packages(
        exclude=(
            "deepnlpf_env",
            "deepnlpf_env_tests"
            "docker",
            "images",
            "tests"
        )
    ),

    include_package_data=True,

    # Create dir.
    data_files=[
        (HOME+'/deepnlpf_data', []),
        (HOME+'/deepnlpf_data/plugins', []),
        (HOME+'/deepnlpf_data/output', [])
    ],

    #install_requires=REQUIRED,

    install_requires=[
        'bson==0.5.9', 'Flask==1.1.2', 'gogo==1.1.1', 'google==2.0.3', 'homura==0.1.5',
        'isodate==0.6.0', 'Jinja2==2.11.1', 'json2xml==3.3.2', 'mongoengine==0.19.1',
        'names==0.3.0', 'pandas==1.0.3', 'path==13.2.0', 'pathos==0.2.5', 'plotly==4.6.0',
        'psutil==5.7.0', 'pygogo==0.12.0', 'pymongo==3.10.1',
        'requests==2.23.0', 'stanza==1.0.0', 'tqdm==4.45.0', 'PyYAML==5.3.1', 'ray==0.8.4'
    ],

    # List required Python versions.
    python_requires='>=3.7',

    entry_points={
        "console_scripts": [
            "deepnlpf=deepnlpf.__main__:main"
        ]
    }

)
