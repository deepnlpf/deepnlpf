# install package locally
    
    python setup.py install --user

# Kill processing

    sudo lsof -t -i tcp:5001 | xargs kill -9

# Commit PyPI

    