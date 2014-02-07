'''
Created on 07/02/2014

@author: Javier
'''

def bench(f):
    def inner(*args, **kwargs):
        from time import time
        begin = time()
        result = f(*args, **kwargs)
        end = time()
        print "Time elapsed: %d ms" % (end - begin)
        return result
    
    return inner
    