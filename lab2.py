'''
Created on Sep 14, 2017
I pledge my honor that I have abided by the Stevens Honor System -Joshua Schmidt
@author: jschmid3@stevens.edu
'''
from cs115 import filter

def dot(L, K):
    """returns the dot product of lists L and K"""
    def dotHelp(L, K, accum):
        if (L == [] or K == []):
            return accum
        return dotHelp(L[1:], K[1:], accum+L[0]*K[0])
    
    return dotHelp(L, K, 0)

print(dot([5,3], [6,4]))

def explode(s):
    """returns a string, but as a list, with one
    character per index"""
    def explodeHelp(s, accum):
        if(s==""):
            return accum
        return explodeHelp(s[1:], accum + [s[0]])
    return explodeHelp(s,[])

print(explode("apple"))

def length(L):
        def lengthHelp(L, num):
            if(L == []):
                return num
            return lengthHelp(L[1:],num+1)
        return lengthHelp(L, 0)

def ind2(e,L):
    """returns the index of an element in a list"""
    def indHelp(e,L,c):
        if(c==len(L)):
            return c
        if(e==True):
            return c
        if(e == L[c]):
            return c
        return indHelp(e,L,c+1)
    return indHelp(e,L,0)

def ind(e,L):
    def indHelp(e,L,c):
        if L == [] or L == "":
            return c
        if L[0] == e:
            return c
        return indHelp(e, L[1:], c+1)
    return indHelp(e, L, 0) 

print(ind(42, [ 55, 77, 42, 12, 42, 100 ]))
print(ind(42, range(0,100)))
print(ind(' ', 'outer exploration'))
print(ind(42, []))
print(ind('hi', ['hello', 42, True]))
print(ind('hi', ['well', 'hi', 'there']))
print(ind('i', 'team'))
print(ind(' ', 'outer exploration'))

def removeAll(e,L):
    """returns the list but without all the e's"""
    def removeHelp(e,L,lst):
        if(L==[]):
            return lst
        if(L[0]==e):
            return removeHelp(e,L[1:], lst)
        return removeHelp(e,L[1:], lst + [L[0]])
    return removeHelp(e,L,[])

print(removeAll(42, [ 55, 77, 42, 11, 42, 88 ]))

def even(x):
    """returns true if even number, false if odd"""
    if(x%2 == 0):
        return True
    else:
        return False
    
print(filter(even, [0, 1, 2, 3, 4, 5, 6]))

def myFilter(f, L):
    """puts a function on each element of list"""
    def filterHelp(f, L, lst):
        if(L == []):
            return lst
        if(f(L[0])==True):
            return filterHelp(f, L[1:], lst + [L[0]])
        else:
            return filterHelp(f, L[1:], lst)
    return filterHelp(f, L, [])

print(myFilter(even, [0, 1, 2, 3, 4, 5, 6]))

"""
def deepReverse(L):
    ""reverses order of list""
    def reverseHelp(L, lst, c):
        if(L == []):
            return lst
        if(isinstance(L[c], list)):
            #if(isinstance(L[1], list)==False):   
            return reverseHelp(L[c:], lst, 0)
        else:
            return reverseHelp(L[c:], [L[c+1]]+lst, c+1)
    return reverseHelp(L, [], 0)
"""

def deepReverse(L):
    """reverses order of list"""
    def reverseHelp(L, lst):
        if(L == []):
            return lst
        if(isinstance(L[0], list)):
            return reverseHelp(L[1:], [deepReverse(L[0])]+lst)
        else:
            return reverseHelp(L[1:], [L[0]]+lst)
    return reverseHelp(L, [])


print(deepReverse([1, [2, [3, 4], [5, [6, 7], 8]]]))