'''
Created on Oct 23, 2017

@author: jschmid3@stevens.edu
Pledge:    I pledge my honor that I have abided by the Stevens Honor System -Joshua Schmidt

CS115 - Hw 7
'''

def numToBase(n, b):
    """converts a number in decimal to base b"""
    if n == 0:
        return '0'
    def numToBaseHelper(n,b):
        """helps the function in making it base b"""
        if n == 0:
            return ""
        if n % b == '0':
            return numToBase(n / b, b) + "0"
        return numToBaseHelper(int(n / b), b) + str(n % b)
    return numToBaseHelper(n, b)

#print(numToBase(13, 3)) #FIX THISwith recursive loop helper

def baseBToNum(n, b):
    """makes a number in base b to decimal"""
    if n == "":
        return 0
    return (int(n[0]))*(b**(len(n)-1))+baseBToNum(n[1:], b)

#print(baseBToNum("0", 10))

def baseToBase(b1, b2, n):
    """takes a number n in base b1 and outputs it in base b2"""
    numInDecimal = baseBToNum(n, b1)
    return numToBase(numInDecimal, b2)

#print(baseToBase(3, 5, "11"))

def add(n1, n2):
    """adds 2 binary numbers using functions above, converting to decimal"""
    decFirstNumber = baseBToNum(n1, 2)
    decSecondNumber = baseBToNum(n2, 2)
    result = decFirstNumber + decSecondNumber
    return numToBase(result, 2)

#print(add("11", "01"))

def addB(n1, n2):
    """adds 2 binary numbers without converting to decimal or using ints"""
    if n1 == "":
        return n2
    elif n2 == "":
        return n1
    elif n1[-1] == "0" and n2[-1] == "0":
        return addB(n1[:-1], n2[:-1]) + '0'
    elif (n1[-1] == "0" and n2[-1] == "1") or (n1[-1] == "1" and n2[-1] == "0"):
        return addB(n1[:-1], n2[:-1]) + '1'
    elif n1[-1] == "1" and n2[-1] == "1":
        return addB(n1[:-1], addB("1", n2[:-1])) + '0'
    else:
        return addB(n1[:-1], addB("1", n2[:-1])) + '1'

print(addB("101110", "100111"))

