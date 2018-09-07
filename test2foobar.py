'''
Created on Sep 19, 2017

@author: jschm
'''
from cs115 import reduce, range
from cmath import sqrt
# solution for problem 1 in level 3
"""
def answer(M, F):
    m = int(M)
    f = int(F)

    if m * f == 0:
        return "impossible"

    g = gcd(m, f)
    if g != 1 and (abs(m - f) % g == 0):
        return "impossible"

    return str(answer_helper(m, f))

def answer_helper(m, f):
    if m == 1:
        return f - 1
    elif f == 1:
        return m - 1
    else:
        if m < f:
            return answer_helper(f, m)
        else:
            return (m / f) + answer_helper(m - m / f * f, f)

def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

print(answer("1", "1"))
print(answer("2", "1"))
print(answer("9", "37"))
"""
"""
def answer(start, length):
    worker_list = [(start + (length - l) * length,
                    start + (length - l) * length + l)
                   for l in range(length, 0, -1)]

    reduced_xor = [xor_range(start, end) for start, end in worker_list]

    return reduce(lambda x, y: x ^ y, reduced_xor)

def xor_range(start, end):
    # inclusive start and exclusive end
    if (end - start) == 0:
        return 0
    if (end - start) == 1:
        return start
    if (end - start) <= 4:
        return reduce(lambda x, y: x ^ y, range(start, end))
    else:
        begin_range = (start, start / 4 * 4 + 4)
        end_range = (end / 4 * 4, end)
        return xor_range(*begin_range) ^ xor_range(*end_range)

print(answer(0, 3))
# print(answer(17, 4))
# print(answer(17, 250))
# print(answer(17, 2500))
"""
"""Escape Pods
===========

You've blown up the LAMBCHOP doomsday device and broken the bunnies out of
Lambda's prison - and now you need to escape from the space station as quickly
and as orderly as possible! The bunnies have all gathered in various locations
throughout the station, and need to make their way towards the seemingly endless
amount of escape pods positioned in other parts of the station. You need to get
the numerous bunnies through the various rooms to the escape pods.
Unfortunately, the corridors between the rooms can only fit so many bunnies at a
time. What's more, many of the corridors were resized to accommodate the
LAMBCHOP, so they vary in how many bunnies can move through them at a time.

Given the starting room numbers of the groups of bunnies, the room numbers of
the escape pods, and how many bunnies can fit through at a time in each
direction of every corridor in between, figure out how many bunnies can safely
make it to the escape pods at a time at peak.

Write a function answer(entrances, exits, path) that takes an array of integers
denoting where the groups of gathered bunnies are, an array of integers denoting
where the escape pods are located, and an array of an array of integers of the
corridors, returning the total number of bunnies that can get through at each
time step as an int. The entrances and exits are disjoint and thus will never
overlap. The path element path[A][B] = C describes that the corridor going from
A to B can fit C bunnies at each time step. There are at most 50 rooms connected
by the corridors and at most 2000000 bunnies that will fit at a time.

For example, if you have:
entrances = [0, 1]
exits = [4, 5]
path = [
  [0, 0, 4, 6, 0, 0],  # Room 0: Bunnies
  [0, 0, 5, 2, 0, 0],  # Room 1: Bunnies
  [0, 0, 0, 0, 4, 4],  # Room 2: Intermediate room
  [0, 0, 0, 0, 6, 6],  # Room 3: Intermediate room
  [0, 0, 0, 0, 0, 0],  # Room 4: Escape pods
  [0, 0, 0, 0, 0, 0],  # Room 5: Escape pods
]

Then in each time step, the following might happen:
0 sends 4/4 bunnies to 2 and 6/6 bunnies to 3
1 sends 4/5 bunnies to 2 and 2/2 bunnies to 3
2 sends 4/4 bunnies to 4 and 4/4 bunnies to 5
3 sends 4/6 bunnies to 4 and 4/6 bunnies to 5

So, in total, 16 bunnies could make it to the escape pods at 4 and 5 at each
time step.  (Note that in this example, room 3 could have sent any variation of
8 bunnies to 4 and 5, such as 2/6 and 6/6, but the final answer remains the
same.)

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (int list) entrances = [0]
    (int list) exits = [3]
    (int) path = [[0, 7, 0, 0], [0, 0, 6, 0], [0, 0, 0, 8], [9, 0, 0, 0]]
Output:
    (int) 6

Inputs:
    (int list) entrances = [0, 1]
    (int list) exits = [4, 5]
    (int) path = [[0, 0, 4, 6, 0, 0], [0, 0, 5, 2, 0, 0], [0, 0, 0, 0, 4, 4], [0, 0, 0, 0, 6, 6], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
Output:
    (int) 16

Use verify [file] to test your solution and see how it does. When you are
finished editing your code, use submit [file] to submit your answer. If your
solution passes the test cases, it will be removed from your home folder.
"""
"""
import decimal
inf = decimal.Decimal("Infinity")

def answer(entrances, exits, path):
    ""this returns the number of bunnies that can fit
    through to the escape pods...This is a pretty complicated
    and involved question thanks for making me struggle google""
    makeSimpler(entrances, exits, path)
    count = 0
    length = len(path)
    numItems = [[0 for i in range(length)] for j in range(length)]
    start = 0
    finish = length - 1
    while True:
        newCount, parents = abc(start, finish, path, numItems)
        if newCount == 0:
            break
        count += newCount
        y = finish
        while y != start:
            x = parents[y]
            numItems[x][y] += newCount
            numItems[y][x] -= newCount
            y = x
    return count

def makeSimpler(entrances, exits, path):
    global inf
    #transform to make the array a single network
    length = len(path)
    entrances = [i + 1 for i in entrances]
    exits = [i + 1 for i in exits]
    for row in path:
        row.insert(0, 0)
        row.append(0)
    start_row = [0] * (length + 2)
    for i in entrances:
        start_row[i] = inf
    path.insert(0, start_row)
    end_row = [0] * (length + 2)
    for i in exits:
        path[i][-1] = inf
    path.append(end_row)
    return entrances, exits, path

def abc(start, finish, path, flows):
    global inf
    length = len(path)
    table = [-1] * length
    #table for reversing path
    table[start] = -2         
    #have new starting point for both

    next = []
    next.append(start)
    while next and table[finish] == -1:
        x = next.pop(0)
        for y in range(length):
            cf = path[x][y] - flows[x][y]
            if cf > 0 and table[y] == -1:
                next.append(y)
                table[y] = x

    if table[finish] == -1:      # if t can not been reached
        return 0, table

    y = finish
    delta = inf
    while y != start:
        x = table[y]
        cf = path[x][y] - flows[x][y]
        delta = min(delta, cf)
        y = x

    return delta, table

print(answer([0], [3], [[0,7,0,0],[0,0,6,0],[0,0,0,8],[9,0,0,0]]))
"""
"""
import itertools

def answer(numBunnies, numRequired):
    ""so I need to get all of the keys based on Commander Lambda's system
    - that is, there are no more keys than necessary, and there are consoles
    to open the cells...""
    theAnswer = []
    lst = list(itertools.combinations(range(numBunnies),numRequired))
    #finds the combinations of the range of numBunnies and numRequired
    total = len(lst)*numRequired
    #gets the number of total in list, based on required
    numRepeat = numBunnies - numRequired + 1
    #have to add one because we are left with 0 sometimes (if it's the same)
    newLst = list(itertools.combinations(range(numBunnies),numRepeat))
    for x in range(numBunnies):
        theAnswer.append([])

    for x in range(total/numRepeat):
        for y in newLst[x]:
            theAnswer[y].append(x)
        #append the answer with the total / numRepeating
    return theAnswer

print(answer(5,3))

"""
"""
#def answer(n):
    #RESEARCH:
    #https://oeis.org/search?q=floor%28n*sqrt%282%29%29&sort=&language=&go=Search
    #http://math.stackexchange.com/questions/2052179/how-to-find-sum-i-1n-left-lfloor-i-sqrt2-right-rfloor-a001951-a-beatty-s
minusSqrt = 4142135623730950488016887242096980785696718753769480731766797379907324784621070388503875343276415727
#100 digits minus squareroot of 2
def divisor(num):
    return (minusSqrt*num) // (10**100)
    #returns the minumSqrt floor divided by 10^100
def recursive(num):
    if num < 1:
        return 0
    if num == 1:
        return 1
    #base cases^
    return num*divisor(num) + (num+1)*num/2 - (divisor(num)+1)/2*divisor(num) - recursive(divisor(num))
    #recursive of num*div + num+1*num/2 - (div+1)/2*div(num) - recursive of div
    #I just took this formula from the stackexchange thing (but translated it...
def answer(n):
    return str(recursive(n))
    
print(answer(77))
"""
"""
import base64
coded_string = '''jacopo.notarstefano'''
coded_string = '''
EUgAHRYCSx1dVENSTU4DBg8OB09ZQQkNQR8PDQwOERFNT0lIUgRdGksWDg0JTkhUTQoVDhoTWh0J U1lISgAKFxgKFwEXDUtJAlNECQ4BDREcCh4NGxUJThRTRB0DBQsXAQoXT1lBCRxPEQEBGRpDVFBP VBsUB0tJAlNEDgIGQ1RQT1QfHA8PSVM= 
'''
print(base64.b64decode(coded_string))
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import base64

MESSAGE = '''
EUgAHRYCSx1dVENSTU4DBg8OB09ZQQkNQR8PDQwOERFNT0lIUgRdGksWDg0JTkhUTQoVDhoTWh0J
U1lISgAKFxgKFwEXDUtJAlNECQ4BDREcCh4NGxUJThRTRB0DBQsXAQoXT1lBCRxPEQEBGRpDVFBP
VBsUB0tJAlNEDgIGQ1RQT1QfHA8PSVM=
'''

KEY = 'joshua.n.schmidt'

result = []
for i, c in enumerate(base64.b64decode(MESSAGE)):
    result.append(chr(ord(chr(c)) ^ ord((KEY[i % len(KEY)]))))

print(''.join(result))