# -*- coding: utf-8 -*-

"""[boost]
    https://realpython.com/python-concurrency/
"""

import psutil, pathos, ray
import pathos.pools as pp

from tqdm import tqdm

class Boost(object):

    def __init__(self):
        self.cpu_count = psutil.cpu_count(logical=False)

    def multithreading(self, function, args, threads=4):
        from concurrent.futures import ThreadPoolExecutor
        
        with ThreadPoolExecutor(max_workers=threads) as executor:
            result = list(tqdm(executor.map(function, args), desc='Processing sentence(s)'))
            
        return result

    def multiprocessing(self, function, tools):
        pool = pp.ProcessPool(self.cpu_count)
        
        #process = str(pathos.helpers.mp.current_process())
        #logs.logger.info("{}, {}".format(process, tool))
        #Telegram().send_message("⛏️ Processing... ForkProcess: {}, {}".format(str(process), str(tool)))
        
        return [_ for _ in tqdm(pool.map(function, tools), total=len(tools), desc='NLP Tool(s)')]

    def parallel(self, function, tools):
        ray.init(num_cpus=self.cpu_count)
        
        @ray.remote
        def f(function, tools):
            return [_ for _ in tqdm(map(function, tools), total=len(tools), desc='NLP Tool(s)')]

        #futures = [f.remote(tool) for tool in tools]
        return ray.get(f.remote(function, tools))
    
    