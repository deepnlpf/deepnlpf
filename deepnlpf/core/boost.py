# -*- coding: utf-8 -*-

"""[boost]
    https://realpython.com/python-concurrency/
"""

from tqdm import tqdm

class Boost(object):

    def __init__(self):
        import psutil
        #import multiprocessing as mp
        
        #self._cpu_count = psutil.cpu_count(logical=False)
        self._cpu_count = psutil.cpu_count()
        #self._cpu_count = mp.cpu_count()

    def multithreading(self, function, args, threads=4):
        from concurrent.futures import ThreadPoolExecutor
        
        with ThreadPoolExecutor(max_workers=threads) as executor:
            result = list(tqdm(executor.map(function, args)))
            
        return result

    def parallelpool(self, function, tools):
        import pathos
        import pathos.pools as pp

        pool = pp.ProcessPool(self._cpu_count)
        
        #process = str(pathos.helpers.mp.current_process())
        #logs.logger.info("{}, {}".format(process, tool))
        #Telegram().send_message("⛏️ Processing... ForkProcess: {}, {}".format(str(process), str(tool)))
        
        return [_ for _ in tqdm(pool.map(function, tools), total=len(tools))]