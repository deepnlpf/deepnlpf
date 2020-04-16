# -*- coding: utf-8 -*-

"""
    Date 16/08/2019
"""

class Execute (object):
    """ Execute Scripts External in Outher Language Programation. """

    def __init__(self):
        pass

    def run_r(self, script, *args):
        import rpy2.robjects as ro
        
        r = ro.r
        r.source(script)
        
        return r.main(*args)

    def run_java(self, jar_file, *args):
        try:
            import subprocess
            
            return subprocess.check_output(['java', '-jar', jar_file, *args], shell=False)
        except Exception as err:
            print(err)