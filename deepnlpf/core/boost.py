# -*- coding: utf-8 -*-

"""[boost]
    https://realpython.com/python-concurrency/
"""

import psutil

from tqdm import tqdm

class Boost(object):

    def __init__(self):
        self.cpu_count = psutil.cpu_count() # logical=False

    def multithreading(self, function, args, threads=4):
        from concurrent.futures import ThreadPoolExecutor
        
        with ThreadPoolExecutor(max_workers=threads) as executor:
            result = list(tqdm(executor.map(function, args), desc='Processing sentence(s)'))
            
        return result
    
    