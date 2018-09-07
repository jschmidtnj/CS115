'''
Created on 10/11/2017
@author:   jschmid3@stevens.edu
Pledge:    I pledge my honor that I have abided by the Stevens Honor System -Joshua Schmidt

CS115 - Lab 6
'''
def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    #question 1: base_2 of 42: 101010
    if n == 0:
        return False
    if n % 2 != 0:
        return True
    return False

#question 2: if given an odd base-10 number, the least-significant bit of its base-2 representation will be a 1.
#question 3: if given an even base-10 number, the least-significant bit of its base-2 representation will be a 0.
#This is because 2^0 = 1, and that is the only way to make an odd number, by having a 1 in the least significant bit.
#question 4: By eliminating the least significant bit, the original number decreases by a factor of 2, if the bit is a 0.
#if the least significant bit is a 1, the original number is decreased by a factor of 2, - 1.
#question 5: If N is odd, the base-2 of N is Y + "1". If N is even, the base-2 of N is Y + "0".
#This is because to get from N base-10 to N base-2 you do successive division by 2, keeping the remainder, so given
#the base-2 of all of the division except for the first, one must put that remainder in front, hence the answer given.

def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if n == 0:
        return ""
    elif isOdd(n):
        return numToBinary(n // 2) + "1"
    else: return numToBinary(n // 2) + "0"
#print(numToBinary(15))

def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if s == "":
        return 0
    return int(s[0])*(2**(len(s)-1)) + binaryToNum(s[1:])
#print(binaryToNum("1111"))

def addBin(s, numAdd, carry = 0):
    """adds 2 binary numbers"""
    if s == "" or numAdd == "":
        if carry == 0:
            return s + numAdd
    place = carry
    carry = 0
    if s != "" and s[-1] == "1":
        carry = place
        place = 1 - place
    if numAdd != "" and numAdd[-1] == "1": 
        carry += place
        place = 1 - place
    return addBin(s[:-1], numAdd[:-1], carry) + str(place)

#print(addBin("100", "001", 0))

def makeEightBit(a):
    """makes a binary number 8 bit"""
    if len(a) == 8:
        print(str(a))
        return str(a)
    elif len(a) > 8:
        #print(a[(len(a)-8):])
        makeEightBit(a[(len(a)-8):])
    else:
        makeEightBit("0" + a)
        return ""

def increment(s):
    '''Precondition: s is a string of 8 bits.
    Returns the binary representation of binaryToNum(s) + 1.'''
    #numAdd = "00000001"
    dec = binaryToNum(s)
    dec += 1
    answer = numToBinary(dec)
    #print(answer)
    if len(answer) > 8:
        return answer[(len(answer)-8):]
    answer = (8-len(answer))*"0" + answer
    return answer
#print(increment("1110100000"))

def count(s, n):
    '''Precondition: s is an 8-bit string and n >= 0.
    Prints s and its n successors.'''
    if n == 0:
        print(s)
        return ""
    print(s)
    return count(increment(s), n-1)
#print(count("11111110", 5))
#print("a")

def numToTernary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the ternary representation of non-negative integer
    n. If n is 0, the empty string is returned.'''
    if n == 0:
        return ""
    return numToTernary(n // 3) + str(n % 3)
#print(numToTernary(42))

def ternaryToNum(s):
    '''Precondition: s is a string of 0s, 1s, and 2s.
    Returns the integer corresponding to the ternary representation in s.
    Note: the empty string represents 0.'''
    if s == "":
        return 0
    return int(s[0])*(3**(len(s)-1)) + ternaryToNum(s[1:])
#print(ternaryToNum('12211010'))
