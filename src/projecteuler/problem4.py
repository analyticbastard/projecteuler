'''
Created on 08/02/2014

@author: Javier
'''

def make_number(cent, dec, unit):
    return cent*100 + dec*10 + unit


def decompose(n):
    vec = []
    for i in range(6):
        vec.append(n % 10)
        n = n / 10
    return vec

def ispalindrome(n):
    vec = decompose(n)
    for i in range(len(vec)):
        if vec[i] != vec[len(vec)-i-1]:
            return False
    return True

def problem4():
    cents = range(1,10)
    decs  = range(10)
    units = range(10)
    
    palindromes = []
    for c1 in cents:
        for d1 in decs:
            for u1 in units:
                n1 = make_number(c1, d1, u1)
                for c2 in cents:
                    for d2 in decs:
                        for u2 in units:
                            n2 = make_number(c2, d2, u2)
                            n = n1 * n2
                            if ispalindrome(n):
                                palindromes.append(n)
    return max(palindromes)
    

print problem4()