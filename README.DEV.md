# Virtualenv
[Tutprial Base](https://pythonacademy.com.br/blog/python-e-virtualenv-como-programar-em-ambientes-virtuais)

    $ virtualenv deepnlpf
    $ source deepnlpf/bin/activate

# Kill processing

    sudo lsof -t -i tcp:5000 | xargs kill -9

# Install package locally
    
    python setup.py install --user

# create even conda

    conda create -n deepnlpf_env python=3 anaconda

# Generated Requeriment

    pip freeze > requirements.txt


# Generating Code Documentation with Pycco
Auto-Generating Documentation for an Entire Project

    pycco deepnlpf/*.py -p
    pycco deepnlpf/**/*.py -p
    
    pycco deepnlpf/**/*.py -p --watch