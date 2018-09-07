'''
Created on 10/15/2017
@author:   jschmid3@stevens.edu
Pledge:    I pledge my honor that I have abided by the Stevens Honor System -Joshua Schmidt

CS115 - Hw 6
'''
from cs115 import reduce
# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 5

# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1

# Do not change the variables above.
# Write your functions here. You may use those variables in your code.

def countRun(s, c, maxRun, count):
    """parameter s: a string
    parameter c: what we're counting
    parameter maxRun: maximum length of run
    returns: the number of times that string occurs in a row"""
    
    """
    trial:
    def countRunHelp(s,c,maxRun, count):
        if count == maxRun:
            return c
        if s[count] == s[count+1]:
            c+=1
        return countRunHelp(s, c, maxRun, count+1)
    return countRunHelp(s, c, maxRun, 0)
    """
    if s == '':
        return 0
    if count >= maxRun:
        return 0
    if s[:len(c)] != c:
        return 0
    return 1 + countRun(s[len(c):], c, maxRun, count + 1)

print(countRun("0"*16 + "0", '0', MAX_RUN_LENGTH, 0))

def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    #question 1: base_2 of 42: 101010
    if n == 0:
        return False
    if n % 2 != 0:
        return True
    return False

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

def add(x, y):
    return x + y

def lengthFix(s):
    if len(s) == COMPRESSED_BLOCK_SIZE:
        return s
    return lengthFix('0' + s)

def compress(s):
    """param s: string to compress
    count the runs in s switching
    from counting runs of zeros to counting runs of ones
    return compressed string"""
    def compress_help(s, c):
        if s == "":
            return ""
        temp = lengthFix(numToBinary(countRun(s,c,MAX_RUN_LENGTH, 0)))
        return temp + compress_help(s[countRun(s, c, MAX_RUN_LENGTH, 0):], '0' if c == '1' else '1')
    return reduce(add, map(numToBinary(compress_help(s, '0'))))

print(compress("0000000000" + '1'))

def uncompress(s):
    """param s: in chunks of COMPRESSED_BLOCK_SIZE, we take COMPRESSED_BLOCK_SIZE many characters at a time,
    then convert these characters from the binary representation of a number into that many zeroes or ones, we do this by 
    switching from outputting zeros to outputting ones alternatively.
    return decompressed string"""
    def uncompress_help(s, c):
        if s == "":
            return 0
        first = s[:COMPRESSED_BLOCK_SIZE]
        temp = binaryToNum(countRun(s, c, MAX_RUN_LENGTH, 0))
        return temp + uncompress_help(s[COMPRESSED_BLOCK_SIZE:], '0' if c == '1' else '1')
    return uncompress_help(s, '0')
    
#print(uncompress([10,1]))
    
def compression(s):
    """return divide compressed size by original size"""
    return len(compress(s)) / len(s)