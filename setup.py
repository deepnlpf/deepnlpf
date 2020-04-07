# -*- coding: utf-8 -*-
from setuptools import setup, Extension, find_packages
from codecs import open
from os import path
import os, re

here = path.abspath(path.dirname(__file__))
HOME = os.environ['HOME']

# read the version from stanza/_version.py
version_file_contents = open(path.join(here, 'deepnlpf/_version.py'), encoding='utf-8').read()
VERSION = re.compile('__version__ = \"(.*)\"').search(version_file_contents).group(1)

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
    keywords='natural-language-processing nlp natural-language-understanding stanford-nlp deep-learning',
    
    # Choose your license
    license="Apache License 2.0",

    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

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
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    packages=find_packages(exclude=("tests", "images")),
    include_package_data=True,

    # create directory plugins.
    data_files=[(HOME+'/deepnlpf_plugins', [])],

    install_requires=REQUIRED,
    
    #install_requires=[
    #    'tqdm', 'bson', 'pygogo', 'homura','pathos', 'gogo', 'pymongo', 'isodate', 'requests', 
    #    'future', 'mongoengine', 'flask', 'pandas', 'plotly', 'names', 'psutil', 'path', 
    #    'json2xml', 'stanza'
    #    ],
    
    
     # List required Python versions
    python_requires='>=3.7',

    entry_points={
        "console_scripts": [
            "deepnlpf=deepnlpf.__main__:main"
        ]
    },
    
)
