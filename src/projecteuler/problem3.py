'''
Created on 06/02/2014

@author: Javier
'''

import numpy as np

def isprime(x, primes):
    if primes[len(primes)-1] == x:
        return True
    primes_sqrt = [e for e in primes if e<np.sqrt(x)]
    for p in primes_sqrt:
        if x % p == 0:
            return False
    return True

def problem3(N):
    #600851475143
    divs = [1]
    rem = N
    while rem % 2 == 0:
        divs += [2]
        rem = rem / 2
    x = 3
    primes = [2]
    while reduce(lambda x,y: x*y, divs ) < N:
        if isprime(x, primes):
            if primes[len(primes)-1] != x:
                primes += [x]
            if rem % x == 0:
                divs += [x]
                print x, "is a factor"
                rem = rem / x
                if rem % x != 0:
                    x += 2
            else:
                x += 2
        else:
            x += 2
    return max(divs)

N = 600851475143
x = problem3(N)
print "Max factor of %d : %d " % (N, x)