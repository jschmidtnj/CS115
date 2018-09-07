'''
Created on Oct 31, 2017

@author: jschmid3@stevens.edu
Pledge:    I pledge my honor that I have abided by the Stevens Honor System -Joshua Schmidt

CS115 - Hw 8
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

def baseBToNum(n, b):
    """makes a number in base b to decimal"""
    if n == "":
        return 0
    return (int(n[0]))*(b**(len(n)-1))+baseBToNum(n[1:], b)

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
    
#print(addB("11111111", "10"))

def toggle(base2Num):
    """toggles a base 2 number"""
    if base2Num == "":
        return ""
    if base2Num[0] == "1":
        return "0" + toggle(base2Num[1:])
    return "1" + toggle(base2Num[1:])

#print(toggle("10000000"))
#print(addB(toggle("10000000"), "1"))

def makeEightBits(base2Num):
    """assumes base2Num is less than 8 bits initially, and makes it 8 bits"""
    if len(base2Num) == 8:
        return base2Num
    return makeEightBits("0" + base2Num)

def TcToNum(input):
    """takes a binary 8-bit input and returns the output (can be negative)"""
    #if the input is negative, flip and add 1
    if input[0] == "1":
        input = addB(toggle(input), "1")
        if len(input) == 8:
            return int(baseBToNum(input, 2) * (-1))
        return int(baseBToNum(input[1:], 2)) * (-1)
    return int(baseBToNum(input[1:], 2))

#print(TcToNum("01000000"))
        
def NumToTc(input):
    """takes an input integer N and returns a base-2 representation"""
    inputBase = 10
    if input >= 128 or input < -128:
        return "Error"
    if input >= 0:
        return makeEightBits(numToBase(input, 2))
    #take positive base2, toggle, add 1
    return addB(toggle(makeEightBits(numToBase(input, 2))), "1")

#print(NumToTc(1))