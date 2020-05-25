"""
    This script uses Ray on a muti-nodes, with parallel processing.
""" 

import ray

# https://docs.ray.io/en/latest/starting-ray.html#using-ray-on-a-cluster
ray.init(address="auto")

@ray.remote
def f(x):
    return x * x

futures = [f.remote(i) for i in range(100)]
print(ray.get(futures))