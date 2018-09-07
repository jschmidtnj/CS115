'''
Created on Sep 18, 2017

@author: jschm
'''
from cs115 import range, reduce
def answer1(x, y):
    # your code here
    id = 0
    for i in range(x):
        id += i + 1
        for j in range(y):
            id += j
    return str((x+y-2)*(x+y-1)/2+x)
print(answer1(5,10))

# solution for problem 3 in level 3
def answer2(n):
    # your code here
    n = int(n) #makes it into an int if it wasn't already
    count = {2: 1, 1: 0}
    def divHelp(n):
        if n in count:
            #if n is 1 or 2 already, return 0 or 1
            return count[n]
        if n % 2 == 0:
            #if n is even, add to count divide by 2 + 1
            count[n] = divHelp(n / 2) + 1
        else:
            #if n is odd, return add to count of the min
            #of adding one, dividing by 2, adding 2, and subtracting
            count[n] = min(divHelp((n + 1) / 2) + 2,
                           divHelp((n - 1) / 2) + 2)
            #need to add 2 so that it does not result in a 0 value
        return count[n]
    return divHelp(n)

print(answer2(15))

def answer3(start, length):
    #list of workers is always from length^2-l+start to that +l
    list_of_workers = [(length * (length - l) + start,
                        length*(length - l) + start + l)
                        for l in range(length, 0, -1)]
    def helper(start, finish):
        if (finish - start == 1): #only 1 long
            return start
        if (finish - start == 0): #no range
            return 0
        if (finish - start < 5): #if length is less than 5, return the power (I don't
            #know why, but this just works
            return reduce(lambda a, b: a ^ b, range(start, finish))
        else:
            #gives the end of the worker list fed into the recursive function
            #this function makes the correct list to look at in the function
            return helper(start, start / 4 * 4 + 4) ^ helper(finish / 4 * 4, finish)
    #the new list is inputted from the helper method, from start to finish
    new_xor = [helper(start, finish) for start, finish in list_of_workers]
    return reduce(lambda a, b: a^b, new_xor)

print(answer3(0,3))

def answer(M,F):
    #put code here
    m = int(M)
    f = int(F)
    #convert strings to ints
    #gets the largest divisor of a and b
    def divisor(a,b):
        if(b==0):
            return a
        return divisor(b, a % b)
    if (m * f) == 0:
        return "impossible"
    a = divisor(m,f)
    #checks if there is no divisor between the two (impossible)
    if (abs(f-m) % a == 0) and a != 1:
        return "impossible"
    
    def helper(m,f):
        #test if M is 1 use F
        if (m == 1):
            return f - 1
        elif (f == 1):
            return m - 1
        #do the same for F
        #what if one is greater than the other?
        if (m < f):
            return helper(f,m)
        return (m / f) + helper(m - m / f * f, f)
        #if M is less than F, flip them
        #otherwise return division + recursion of F and M with whatever remainders left
    return str(helper(m,f))
print(answer("1", "1"))
print(answer("2", "1"))