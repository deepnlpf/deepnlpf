#https://jiffyclub.github.io/snakeviz/

import os, pathlib

PATH_BASE = str(pathlib.Path.cwd())

try:
    # run generated cprofile.
    os.system('python -m cProfile -o ' + PATH_BASE+'/banchmarking_boost_ray.prof' + ' ' + 'pipeline_boost.py')
    
    # view result.
    os.system('cd ' + PATH_BASE + ' && snakeviz ' + 'banchmarking_boost_ray.prof')
except Exception as err:
    print(err)
