'''
Created on Oct 3, 2017

@author: jschm
'''
import time
import sys
sys.setrecursionlimit(100000)

def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

#print(fib(40))
#2^n recursive calls required

def fib_memo(n):
    def fib_helper(n, memo):
        if n in memo:
            return memo[n]
        if n <= 1:
            result = n
        else:
            result = fib_helper(n-1, memo) + fib_helper(n-2, memo)
        memo[n] = result
        return result
    #pass in empty dictionary
    return fib_helper(n, {})

print(fib_memo(6301))
print(fib_memo(900))

def LCS(S1, S2):
    """returns the length of the longest common subsequence in strings S1 and S2. """
    if S1 == '' or S2 == '':
        return 0
    if S1[0] == S2[0]:
        return 1 + LCS(S1[1:], S2[1:])
    return max(LCS(S1, S2[1:]), LCS(S1[1:], S2))

#print(LCS("asdfasdfadsvnakjfvnadfnvak", "asdkfjkalshgkncdjkfaegbejkerb"))

def LCSmemo(S1, S2):
    def LCShelper(S1, S2, memo):
        if (S1, S2) in memo:
            return memo[(S1, S2)]
        if S1 == '' or S2 == '':
            result = 0
        elif S1[0] == S2[0]:
            result = 1 + LCShelper(S1[1:], S2[1:], memo)
        else:
            result = max(LCShelper(S1, S2[1:], memo), LCShelper(S1[1:], S2, memo))
        memo[(S1, S2)] = result
        return result
    
    return LCShelper(S1, S2, {})

print(LCSmemo("asdfasdfadsvnakjfvnadfnvak", "asdkfjkalshgkncdjkfaegbejk"))

def subset_memo(target, lst):
    '''determines whether or not it is possible to create target sum using the values in the list
    values in the list can be positive, negative or zero'''
    last = len(lst)-1
    def subset_helper(target, current, memo):
        if (target, current) in memo:
            return memo[(target, current)]
        if target == 0:
            result = True
        elif current > last:
            result = False
        else:
            result = subset_helper(target - lst[current], current + 1, memo) or \
                    subset_helper(target, current + 1, memo)
        memo[(target, current)] = result
        return result
    return subset_helper(target, 0, {})

def subset_with_values_memo(target, lst):
    last = len(lst)-1
    def subset_helper(target, current, memo):
        if (target, current) in memo:
            return memo[(target, current)]
        if target == 0:
            result = (True, []) #returns tupple this time!
        elif current > last:
            result = (False, [])
        else:
            use_it = subset_helper(target - lst[current], current + 1, memo)
            if use_it[0]:
                result = (True, [lst[current]] + use_it[1])
            else:
                result = subset_helper(target, current + 1, memo)
        memo[(target, current)] = result
        return result
    return subset_helper(target, 0, {})

if __name__ == '__main__':
    start_time = time.time()
    print(subset_memo(100000, list(range(550))))
    print('Computation time with memoization', time.time() - start_time, 'seconds')
    start_time = time.time()
    print(subset_with_values_memo(100000, list(range(550))))
    print('Computation time with values memoization', time.time() - start_time, 'seconds')
    
    