'''
Created on Oct 26, 2017

@author: jschm
'''
start = 8


prev = 0
next = 1
current = 0
if start == 0:
    print(0)
    exit()
    
elif start-1 == 0:
    print(0)
    print(1)
    exit()

elif start-1 > 0:
    print(0)
    print(1)
    start=start-1

def fib(n):
    global start
    global prev
    global next
    global current
    if n == 0:
        exit()
    current = prev + next
    print(current)
    prev = next
    next = current
    fib(n-1)

print(fib(start))

