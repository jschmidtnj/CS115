'''
Created on Sep 12, 2017

@author: jschm
'''
import math
from cs115 import range, map, reduce, filter
#recursive factorial
def tower(n):
    """computes 2^(2^(2^...)) with n twos, using recursion"""
    if(n==0):
        return 1
    return 2**tower(n-1)

print(tower(4))

#callstack, stackframe, recursive call, pending operation, pop, pushing

print(map(tower, range(5)))

def tower_reduce(n):
    def power(x, y):
        return y ** x #instead of x to the y do y to the x - draw it out
    if(n==0):
        return 1
    return reduce(power, [2] * n)
#making a list of twos n long, and multiplying it together

print(map(tower_reduce, range(5)))

def length(lst):
    """returns the length of a list"""
    if(lst == []):
        return 0
    return 1 + length(lst[1:])

print(length([1,42,"spam"]))

def reverse(lst):
    """returns the input of a list of elements, but in reverse order"""
    if(lst == []):
        return []
    return reverse(lst[1:]) + [lst[0]]
    #add first index to the end - this works because the lst is not updated
    #until the end!!!

print(reverse([1,2,3,4]))
    
def member(x,lst):
    """returns true 
    if x is contained in a list and false otherwise"""
    if(lst==[]): #empty list always goes first
        return False
    if(lst[0]==x): #2 base cases
        return True
    return member(x,lst[1:])
#No pending operations - tailing operations :) - good for optimization

print(member(4, [1,3,4,99]))

#Linear recursion:

def power(x,y):
    """returns x^y"""
    if(y==0):
        return 1
    return x *power(x, y - 1)

print(power(2,5))

#tail recursion

def power_tail(x,y):
    """return x^y with tail recursion"""
    def power_tail_helper(x, y, accum):
        if(y==0):
            return accum
        return power_tail_helper(x, y-1, x*accum)
    return power_tail_helper(x, y, 1)

def my_map(f, lst):
    """this does something to every object in a list"""
    if(lst == []):
        return []
    return [f(lst[0])] + my_map(f, lst[1:])
#               ^ "listify"

def my_reduce(f, lst):
    def my_reduce_helper(f, lst, accum):
        if lst == []:
            return accum
        return my_reduce_helper(f, lst[1:], f(lst[0], accum))
    if(lst==[]):
        raise TypeError('my_reduce() of empty sequence with no initial value')
    #   ^ can't reduce something that's already nothhng
    return my_reduce_helper(f, lst[1:], lst[0])

print(my_reduce(sum, [5]))
#-mrh(sum, [], 5)
#--------------
#mrh(sum, [], 5)
#-5

lst = [0,1,2,3,4,8,10,11,13,14]
#print(filter(lambda s: len(s) == 1, lst))
print(filter(lambda x: x % 2 != 0, lst))

def prime(n):
    """return whether or not an integer is prime"""
    possible_divisors = range(2, int(math.sqrt(n)))
    divisors = filter(lambda x: n % x == 0, possible_divisors)
    if(divisors == []):
        return True
    return len(divisors) == 0

print(prime(331))

def primes(n):
    """returns a list of primes in the range [2,n] computed via the sieve of
    Erathosthenes. - pronounced civ (civ 5)"""
    def sieve(lst):
        if lst == []:
            return []
        return [lst[0]] + sieve(filter(lambda x: x % lst[0] != 0, lst[1:]))
    return sieve(range(2, n + 1))
print(primes(947))

def fib(n):
    if(n <= 1):
        return n
    return fib(n-1) + fib(n-2)

print(fib(8))