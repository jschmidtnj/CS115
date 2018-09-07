'''
Created on Oct 23, 2017

@author: jschm
'''
import time
import sys
sys.setrecursionlimit(100000)

def words(input, data):
    if input == []:
        return 0
    def wordHelper(input, data):
        if data == []:
            return 0
        if input == data[0]:
            return 1 + wordHelper(input, data[1:])
        return wordHelper(input, data[1:])
    return wordHelper(input[0], data) + words(input[1:], data)

#print(words(["a", "b", "c"], ["a", "b", "a", "b", "e", "a", "c"]))

"""
put into a text file, 
"""
"""
#HOW DO I MEMOIZE THIS? - ask someone...
def wordsWithMemoization(input, data):
    def wordMemoHelp(input, data, memo):
        if (input, data) in memo:
            return memo[(input, data)]
        if input == []:
            result = 0
        def wordHelper(input, data):
            if data == []:
                result = 0
            if input == data[0]:
                result = 1 + wordHelper(input, data[1:])
            return wordHelper(input, data[1:])
        result = wordHelper(input[0], data) + words(input[1:], data)
        memo[input, data] = result
        return result
    return wordMemoHelp(input, data, {})
"""

#print(wordsWithMemoization(["a", "b", "c"], ["a", "b", "a", "b", "e", "a", "c"]))

"""
data below (can put into a text file and import it
inputs = ["a", "b", "c"]
data = ["a", "b", "a", "b", "e", "a", "c"]
"""

inputs = []
data = []

if __name__ == '__main__':
    f = open('inputs.txt')
    for word in f:
        inputs.append(word.strip())
    f.close
    f = open('data.txt')
    for word in f:
        data.append(word.strip())
    f.close
    start_time = time.time()
    print(words(inputs, data))
    print('Computation time without memoization', time.time() - start_time, 'seconds')
    start_time = time.time()
    #print(wordsWithMemoization(inputs, data))
    print('Computation time with memoization', time.time() - start_time, 'seconds')

