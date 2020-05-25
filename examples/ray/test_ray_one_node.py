"""
    This script uses Ray on a one node, with parallel processing.
""" 

import ray
ray.init()

@ray.remote
def f(x):
    return x * x

futures = [f.remote(i) for i in range(100)]
print(ray.get(futures))