'''
Created on Sep 8, 2017

@author: jschm
'''
#I pledge my honor that I have abided by the Stevens Honor System -Joshua Schmidt
from cs115 import map, reduce
import math
def mult(x, y):
    """returns the product of x and y"""
    return x * y

def add(x, y):
    """returns the sum of x and y"""
    return x + y

def factorial(n):
    """return the factorial of n"""
    return reduce(mult, range(1, n + 1))

def mean(L):
    """return the average of a list"""
    return reduce(add, L)/len(L)

def divides(n):
    """return if n is divisible by k"""
    def div(k):
        return n % k == 0
    return div

def prime(n):
    """returns true if prime number, false otherwise"""
    if n<2:
        return False
    return sum(map(divides(n), range(2, int(math.sqrt(n))+1))) == 0

    """
    def mod(x):
        if(n % x!=0):
            return 0 #if there is a remainder return false
        return 1
            
    return reduce(add, map(mod, (range(2,n))))==0
    """
    """WITH LOOPS"
    for x in range(2,n):
        if divides(n)(x) == True:
            return False
        
    return True
    """
"""
print(factorial(4))
print(mean([1,2,3,4]))
print(divides(4)(2))
print(prime(30))
"""