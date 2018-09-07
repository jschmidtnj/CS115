'''
Created on Sep 7, 2017

@author: jschm
'''
#I pledge my honor that I have abided by the Stevens Honor System -Joshua Schmidt
from cs115 import map, reduce
import math

def add(a,b):
    """returns the sum of a and b"""
    return a + b

def inverse(n):
    """returns the inverse of n"""
    return 1/n

def e(n):
    """returns the sum of the inverses of the factorials of
    integers from 0 to n - the taylor series sum to approximate
    e to an accuracy given by n"""
    return reduce(add, map(inverse, map(math.factorial, range(0, n+1))))

def error(n):
    """returns the absolute value of the taylor estimate and the
    value given by the math.e function, which is assumed to be correct
     - used to find the error of the taylor series approximation function"""
    return abs(e(n)-math.e)

#test
print(e(3))
#print(error(3))