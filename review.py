'''
Created on Sep 25, 2017

@author: jschm
'''
from cs115 import *
from distutils.command.check import check

print(range(5))
"""equivalent to range(0,5,1) or range(0,5)
"""
#[0,1,2,3,4] or [0,5)
print(range(1,6))
#[1,2,3,4,5] or [1,6)
print(range(10,5,-1))
#start, stop, step
#[10,9,8,7,6] or [10.5)
#goes down by -1 for the range
def f(x):
    return x
L = [1,2,3,4,5]
map(f, L)
"""f = function, L = iterable"""
print(map(lambda x: x ** 2, range(6)))
#don't have to create another function to use lambda
#same as saying:
def square(x):
    return x ** 2
print(filter(f,L))
print(filter(lambda s: s[-1] == '!', ['hi', 'hi!', 'review!']))
#if last index is !, don't filter it out
#reduce(f,l)
print(reduce(lambda x,y: x+y, range(7)))
#has 2 parameters to reduce the list

#the sum of odd numbers squared from 1 to 7, including 7
#range(1,8,2) same as filter function below
#OR
print(reduce(lambda x,y: x + y, map(lambda x: x * x, filter(lambda x: x % 2 != 0, range(1,8)))))
L = range(1,7) #[1,2,3,4,5,6]
        #index #:0 1 2 3 4 5
    #back index: -6-5-4-3-2-1
print(L[5])
print(L[-1])
print(L[2:])
print(L[:-2])#[1,2,3,4]
print(L[1:3])#[2,3]
print(L[:])#fresh copy of list
print(L[::2])#get every other
print(L[::1])#get everything single in list

"""RECURSION - there are only really 2 different types - linear and tree
linear:
look at L, L[0], L[1:]
^for nearly all recursion look at that
need base case and recursive test, along with a check
should think about what you are actually recursing over (a list, etc.)
think about what you are returning and make sure it is consistent
"""

def myfilter(f,L):
    if L == []:
        return []
    if f(L[0]): # == True
        return [L[0]] + myfilter(f,L[1:])
    return myfilter(f, L[1:])

def even(x):
    return x % 2 == 0

print(myfilter(even, [0,1,2,3,4]))

#tree
def fib(n):
    if n<2:
        return n
    return fib(n-1)+fib(n-2)

def fun(n):
    if n <= 1:
        print('bye')
        return
    fun(n-1)
    print('hi')
print(fun(3))
#recursive call is fun(n-1), after that there is nothing - so no recursive call

def fun2(n):
    if n <= 1:
        print('bye')
        return
    fun2(n-1)
    print('hi')
    fun2(n-1)
#tree recursion
print(fun2(3))

def fun3(n):
    if n <= 1:
        print('bye')
        return
    fun3(n-1)
#tail recursion because there is nothing after the recursive call...

