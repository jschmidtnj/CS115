
'''
Created on Oct 16, 2017
@author:
'''

def countRun(s, c, maxRun):
    """parameter s: a string
    parameter c: what we're counting
    parameter maxRun: maximum length of run
    returns: the number of times that string occurs in a row"""
    pass
    
def compress(s, c):
    """param s: string to compress
    count the runs in s switching
    from counting runs of zeros to counting runs of ones
    return compressed string"""
    def compress_help(s, c):
        if s == "":
            return []
        runLen = countRun(s, c, MAX_RUN_LENGTH)
        nextC = '0'
        if c == '0':
            nextC = '1'
        return [runLen] + compress_help(s[runLen:], nextC)
    return compress_help(s, '0')
    
def uncompress(s):
    """param s: in chunks of COMPRESSED_BLOCK_SIZE, we take COMPRESSED_BLOCK_SIZE many characters at a time,
    then conver these characters from the binary representation of a number into that many zeroes or ones, we do this by 
    switching from outputting zeros to outputting ones alternatively.
    return decompressed string"""
    def uncompress_help(s, c):
        first5 = s[:COMPRESSED_BLOCK_SIZE]
        temp = something(first5)
        return temp + uncompress_help(s[COMPRESSED_BLOCK_SIZE:], nextC)
    pass
    
def compression(s):
    """return divide compressed size by original size"""