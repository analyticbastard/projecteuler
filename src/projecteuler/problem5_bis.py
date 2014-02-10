'''
Created on 07/02/2014

@author: Javier
'''

from utils.bench import bench

def gcd(*numbers):
    """Return the greatest common divisor of the given integers"""
    from fractions import gcd
    return reduce(gcd, numbers)

def lcm(*numbers):
    """Return lowest common multiple."""
    def lcm(a, b):
        return (a * b) // gcd(a, b)
    return reduce(lcm, numbers, 1)

@bench
def problem5(N):
    args = range(2,N)
    return lcm(*args)

x = problem5(20)
print "Least common multiple is", x