# Virtualenv
    https://pythonacademy.com.br/blog/python-e-virtualenv-como-programar-em-ambientes-virtuais

    $ virtualenv deepnlpf
    $ source deepnlpf/bin/activate

# Kill processing

    sudo lsof -t -i tcp:5001 | xargs kill -9

# install package locally
    
    python setup.py install --user

# create even conda

    conda create -n deepnlpf2_t python=3.7 anaconda

# Commit PyPI

    https://python-packaging-tutorial.readthedocs.io/en/latest/uploading_pypi.html
    https://medium.com/@thucnc/how-to-publish-your-own-python-package-to-pypi-4318868210f9


    update
        python setup.py install --user && python3 setup.py sdist bdist_wheel && twine upload dist/*

# Requeriment

    pip freeze > requirements.txt


# Errors

    ImportError: cannot import name 'abc'

        pip uninstall bson
        pip uninstall pymongo
        conda install -c anaconda pymongo 

# Deploy App Flask Enginx in AWS EC2 or Azure

    https://www.youtube.com/watch?v=tW6jtOOGVJI&list=PL5KTLzN85O4KTCYzsWZPTP0BfRj6I_yUP&index=4

    $ cd /etc/nginx/sites-available
    $ sudo nano deepnlpf_api

    server {
        listen 80;
        server_name http://191.232.188.105/;

        location / {
            proxy_pass http://127.0.0.1:5000;
        }
    }

    $ sudo service nginx restart