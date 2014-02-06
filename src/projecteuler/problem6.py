'''
Created on 06/02/2014

@author: Javier
'''

import numpy as np

def problem6(n):
    sum_of_squares = n*(n+1)*(2*n+1)/6;
    sum = n*(n+1)/2
    square_of_sum = sum**2;
    return square_of_sum - sum_of_squares

print "Square of sum minus sum of squares:", problem6(100)