import numpy as np
import psutil, ray
import scipy.signal

num_cpus = psutil.cpu_count(logical=False)

ray.init(num_cpus=num_cpus)

@ray.remote
def f(image, random_filter):
    # Do some image processing.
    print(">")
    return scipy.signal.convolve2d(image, random_filter)[::5, ::5]

filters = [np.random.normal(size=(4, 4)) for _ in range(num_cpus)]

# Time the code below.

for x in range(10):
    print(x)
    image = np.zeros((3000, 3000))
    image_id = ray.put(image)
    ray.get([f.remote(image_id, filters[i]) for i in range(num_cpus)])