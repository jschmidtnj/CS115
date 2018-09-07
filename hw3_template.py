'''
Created on 9/27/17
@author:   jschmid3@stevens.edu
Pledge:    I pledge my honor that I have abided by the Stevens Honor System -Joshua Schmidt

CS115 - Hw 3
'''
# Be sure to submit hw3.py.  Remove the '_template' from the file name.

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 0
' Implement the function giveChange() here:
' See the PDF in Canvas for more details.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# your code goes here

from cs115 import map

def giveChange(value, coins):
    """Determines whether or not it is possible to create the target value using
    values of coins in the list. Values in the list cannot be negative.
    The function returns a tuple of exactly two items. The first is a count
    of the number of coins needed and false if it is not. The second
    element in the tuple is a list of all values that add up to make the target sum."""
    if value == 0:
        return [0, []]
    elif coins == []:
        return[float('inf'), []]
    elif coins[0] > value:
        return giveChange(value, coins[1:])
    result = giveChange(value - coins[0], coins)
    use_it = [1 + result[0], [coins[0]] + result[1]]
    lose_it = giveChange(value, coins[1:])
    if use_it[0] < lose_it[0]:
        return use_it
    return lose_it


print(giveChange(48, [1, 5, 10, 25, 50]))
# Here's the list of letter values and a small dictionary to use.
# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 1
' Implement wordsWithScore() which is specified below.
' Hints: Use map. Feel free to use some of the functions you did for
' homework 2 (Scrabble Scoring). As always, include any helper
' functions in this file, so we can test it.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def wordsWithScore(dct, scores):
    '''List of words in dct, with their Scrabble score.

    Assume dct is a list of words and scores is a list of [letter,number]
    pairs. Return the dictionary annotated so each word is paired with its
    value. For example, wordsWithScore(Dictionary, scrabbleScores) should
    return [['a', 1], ['am', 4], ['at', 2] ...etc... ]
    '''
    # Implement your functions here.
    def letterScore(letter, scorelist):
        """gets the score for a certain letter in the list"""
        if scorelist == []:
            return 0
        first = scorelist[0]
        if first[0] == letter:
            return first[1]
        return letterScore(letter, scorelist[1:])
    
    #print(letterScore('c', scrabbleScores))
    
    def wordScore(S):
        """gets score of word given a string"""
        if S == "":
            return ['', 0]
        return [S, letterScore(S[0], scores) + wordScore(S[1:])[1]]
    
    #print(wordScore("wow", [['o', 10], ['w', 42]]))
    
    return map(wordScore, dct)

print(wordsWithScore(Dictionary, scrabbleScores))

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 2
' For the sake of an exercise, we will implement a function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
n = 3
L = [1,2,3,4,6,7,8]
def take(n, L):
    '''Returns the list L[0:n].'''
    if L == [] or n == 0:
        return []
    return [L[0]] + take(n-1, L[1:])


#print(L[0:n])
print(take(n, L))

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 3
' Similar to problem 2, will implement another function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def drop(n, L):
    '''Returns the list L[n:].'''
    if n == 0:
        return L
    return drop(n-1, L[1:])

#print(L[n:])
print(drop(n, L))
