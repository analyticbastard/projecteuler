'''
Created on 07/02/2014

@author: Javier
'''

import numpy as np
from utils.bench import bench

def isprime(x, primes):
    if primes[len(primes)-1] == x:
        return True
    primes_sqrt = [e for e in primes if e<=np.sqrt(x)]
    for p in primes_sqrt:
        if x % p == 0:
            return False
    return True

def factors(x, primes):
    facts = {}
    for p in primes:
        if p==1: continue
        while x % p == 0:
            x = x / p
            try:
                facts[p] += 1
            except:
                facts[p] = 1
    return facts

@bench
def problem5(N):
    facts = {2: 1}
    primes = [2]
    nums = range(3,N)
    for n in nums:
        if isprime(n, primes):
            primes += [n]
        nfacts = factors(n, primes)
        keys = [key for key, item in nfacts.iteritems()]
        for key in keys:
            try:
                facts[key] = nfacts[key] if nfacts[key]>facts[key] else facts[key]
            except:
                facts[key] = nfacts[key]
    print "Set of factors:", facts
    norep_facts = reduce(lambda x,y: x+y,
                         [[key] * val for key, val in facts.iteritems()])
    return reduce(lambda x,y: x*y, norep_facts)

mcm = problem5(20)
print "Least common multiple: ", mcm