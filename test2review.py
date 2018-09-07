'''
Created on Oct 24, 2017

@author: jschm
'''
#2 types of use it or lose it - power set and knapsack sort of
#going down one path here and another path there, slightly altering the info for
#these paths
"""
CHEAT SHEET!!!!!!!!!!
-> put use it or lose it on one side (all of it)
then dictionary, memoization, circuit, unittest, binary on the other
"""

"""
use the coin, or lose the coin
powerset - go down a single side, but use it in 2 different ways
"""
from cs115 import map
import sys
sys.setrecursionlimit(100000)

import unittest

def powerset(lst):
    """typically L=['one', 'two'] - return list of lists
    
    """
    if lst == []:
        return [[]] #return empty list of list
    lose_it = powerset(lst[1:]) #lost the first element in the list
    use_it = map(lambda x: [lst[0]] + x, lose_it) #add the first element to the lose_it
    return lose_it + use_it
"""just linear recursion, not tree
    trace: powerset([1,2])
            lose_it = powerset([2]) -> lose_it = powerset([]) -> [[]]
            use_it = [[2]] -> [[2], []] -> [[2], [1,2], [1], []]
"""

print(powerset([1, 2]))

lst = [1,2,3,4]
print(map(lambda x: lst[3] + x, range(1,5)))
#lambda is a temporary function

def getCoins(lst, n):
    if n == 0:
        return 0
    if lst == []:
        return float('inf') #largest number in python - impossible
    if lst[0] > n:
        return getCoins(lst[1:], n)
    use_it = 1 + getCoins(lst[1:], n-lst[1])
    lose_it = getCoins(lst[1:], n)
    return min(use_it, lose_it)

print(getCoins([1,10,15,30], 25))

#dict = {key: value}
dict = {}
dict["steve"] = 19
dict[(11,2)] = "a"
dict["steve"] = [2,19]
print(dict["steve"][1]) #19
tup = (1,2)

def fib(n):
    """generic fibonacci"""
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)
print(fib(8))

def fibWithMemo(n):
    def fibHelper(n, memo):
        if n in memo:
            return memo[n]
        if n < 2:
            result = n
        else:
            result = fibHelper(n-1, memo) + fibHelper(n-2, memo)
        memo[n] = result
        return result
    return fibHelper(n, {})

print(fibWithMemo(6000))

def subset(target, lst):
    """use it or lose it - determines whether or not it is possible to create
    target sum using the values in the list. Values in list can be positive,
    negative or zero"""
    if target == 0:
        return True
    if lst == []:
        return False
    #        use-it                            lose-it (come back to later
    return subset(target - lst[0], lst[1:]) or subset(target, lst[1:])

def subset_with_values(target, lst):
    """determines whether or not it is possible to create the target sum using
    the values in the list. Values in the list can be positive, negative or 0.
    The function returns a tuple of the boolean and the second the values for the sum"""
    if target == "0":
        return (True, [])
    if lst == []:
        return (False, [])
    use_it = subset_with_values(target - lst[0], lst[1:])
    if use_it[0]:
        return (True, [lst[0]] + use_it[1])
    return subset_with_values(target, lst[1:])

#import unittest

def isEven(n):
    return n%2 == 0

class tests(unittest.TestCase):
    def test1(self):
        self.assertTrue(isEven(8))
        self.assertFalse(isEven(7))
        self.assertEqual(isEven(8),True)
    
if __name__ == "__main__":
    unittest.main()
