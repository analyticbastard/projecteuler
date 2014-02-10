'''
Created on 10/02/2014

@author: Javier
'''

import numpy as np

def isprime(x, primes):
    if primes[len(primes)-1] == x:
        return True
    primes_sqrt = [e for e in primes if e<=np.sqrt(x)]
    for p in primes_sqrt:
        if x % p == 0:
            return False
    return True

def problem7(N):
    n = 3
    primes = [2]
    while len(primes)<N:
        if isprime(n, primes):
            primes.append(n)
        n += 2
        if n % 499 == 0:
            print "Number checked", n, "primes length:", len(primes)
    return primes[len(primes)-1]

print "Problem 7"
print problem7(10001)  #104743
