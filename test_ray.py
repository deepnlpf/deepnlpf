import ray
import time

# redis, funcsigs

ray.init()
@ray.remote
def f(i):
    time.sleep(1)
    return i

futures = [f.remote(i) for i in range(4)]

print(ray.get(futures))