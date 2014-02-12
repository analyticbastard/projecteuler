'''
Created on 10/02/2014

@author: Javier
'''

from compiler.ast import flatten
import numpy as np

def problem9(N):
    v = range(1,N)
    # The following just consumes too much memory
    #x = map(lambda a: map(lambda b: map(lambda c: {"a":a, "b":b, "c":c}, v), v), v)
    #y = filter(lambda z: z["a"] + z["b"] + z["c"] == N, flatten(x))
    #z = filter(lambda z: z["a"]**2 + z["b"]**2 == z["c"]**2, y)
    x = []
    for a in v:
        for b in v:
            for c in v:
                if a+b+c==N and a**2 + b**2 == c**2:
                    x.append({"a": a, "b": b, "c": c})
                    print a, b, c
    return np.prod([v for k,v in x[0].iteritems()])
    
    
print "The product is", problem9(1000)