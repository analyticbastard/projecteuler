'''
Created on 06/02/2014

@author: Javier
'''

import numpy as np

def problem1():
    N3 = 333
    sum_three = 3*(N3 * (N3+1))/2
    five_list = range(1,199+1)
    five_less_three = np.setdiff1d(five_list, map(lambda x : x*3, range(1,N3)),True)
    sum_five = 5*np.sum(five_less_three)
    total = sum_three + sum_five
    print sum_three, sum_five, total
    return total
    