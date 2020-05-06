rm -r build && \
rm -r deepnlpf.egg-info && \
rm -r dist && \

python setup.py install --user && \ 
python setup.py sdist bdist_wheel && \
twine upload dist/*