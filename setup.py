from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='deepnlpf',
    packages=['deepnlpf', 'stanfordcorenlp'],
    version='2.0.0',
    description='A Framework for Integrating Linguistic Analysis and Semantic Annotation of Text Documents.',

    author='RodriguesFAS',
    author_email='fasr@cin.ufpe.br',

    url='https://deepnlpf.github.io/site/',
    keywords=['NLP', 'natural language processing', 'computational linguistics'],
    install_requires=['psutil', 'requests'],

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Text Processing',
        'Topic :: Text Processing :: Linguistic',
    ],

    license="MIT License",

    entry_points = {
		'console_scripts': [
			'deepnlpf = deepnlpf.__main__:main'
			]
		}

)