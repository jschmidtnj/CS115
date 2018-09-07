'''
Created on 10/15/2017
@author:   jschmid3@stevens.edu
Pledge:    I pledge my honor that I have abided by the Stevens Honor System -Joshua Schmidt

CS115 - Hw 6
'''
#from cs115 import reduce
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
    returns: the number of times that string occurs in a row
    This is the first step in the run sequence"""
    
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

#print(countRun("0"*16 + "0", '0', MAX_RUN_LENGTH, 0))

def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.
    This makes a number into binary...'''
    if n == 0:
        return ""
    if n % 2 == 0: #if it is divisible by 2
        return numToBinary(n/2) + '0'
    return numToBinary((n-1)/2) + '1'
#print(numToBinary(15))

def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.
    makes a binary number into a base 10 number'''
    if s == "":
        return 0
    if s[-1] == '0':
        return 2 * binaryToNum(s[:-1])
    return 2 * binaryToNum(s[:-1]) + 1
#print(binaryToNum("1111"))

"""
don't need this anymore
def add(x, y):
    #add function
    return x + y
"""

def compress(s):
    """param s: string to compress
    count the runs in s switching
    from counting runs of zeros to counting runs of ones
    return compressed string"""
    #the largest number of bits the compress algorithm can use
    #to encode a 64-bit string or image is 320 bits
    #I tested the penguin and got a compression ratio of 1.484375
    #the smile gave a ratio of 1.328125
    #the five gave a ratio of 1.015625
    #if there is a compression algorithm that could always make a file smaller.
    #then the compression operation would be able to reduce a file to 0 bytes
    #and retain all of the data. However, because 0 bytes does not have any information.
    #there cannot be a compression algorithm to make it smaller. Hence it does not exist.
    
    def lenHelp(s):
        if len(s) == COMPRESSED_BLOCK_SIZE:
            return s
        return lenHelp('0' + s)
    def compress_help(s, c):
        if s == "":
            return ""
        x = lenHelp(numToBinary(countRun(s,c,MAX_RUN_LENGTH, 0)))
        return x + compress_help(s[countRun(s, c, MAX_RUN_LENGTH, 0):], '0' if c == '1' else '1')
    return compress_help(s, '0')

#print(compress("1"*9 + "0"*7 + "10000000"*2 + "1"*7 + "0" + "00000001"*2 + "1"*7 + "0"))

def uncompress(s):
    """param s: in chunks of COMPRESSED_BLOCK_SIZE, we take COMPRESSED_BLOCK_SIZE many characters at a time,
    then convert these characters from the binary representation of a number into that many zeroes or ones, we do this by 
    switching from outputting zeros to outputting ones alternatively.
    return decompressed string
    UNCOMPRESS STRING"""
    def uncompress_help(s, c):
        if s == "":
            return ""
        y = binaryToNum(s[:COMPRESSED_BLOCK_SIZE]) * c
        return y + uncompress_help(s[COMPRESSED_BLOCK_SIZE:], '0' if c == '1' else '1')
    return uncompress_help(s, '0')
    
#print(uncompress([10,1]))
    
def compression(s):
    """return divide compressed size by original size"""
    return len(compress(s)) / len(s)


