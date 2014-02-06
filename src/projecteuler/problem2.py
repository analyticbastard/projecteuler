'''
Created on 06/02/2014

@author: Javier
'''

def problem2():
    MAX = 4000000
    prev = [1,1]
    x = 2
    j = 3
    s = 0
    while x<MAX:
        if j % 3 == 0:
            s += x
        j += 1
        prev[0] = prev[1]
        prev[1] = x
        x = prev[0] + prev[1]
    print s
    return s
    