'''
Created on 9/16/17
@author:   jschmid3@stevens.edu
Pledge:    I pledge my honor that I have abided by the Stevens Honor System -Joshua Schmidt

CS115 - Hw 2
'''
import sys
from cs115 import *
from bigdict import *
# Be sure to submit hw2.py.  Remove the '_template' from the file name.

# Allows up to 10000 recursive calls.
# The maximum permitted limit varies from system to system.
sys.setrecursionlimit(10000)

# Leave the following lists in place.

scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]
"""
Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']
              
"""

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

def wordScore(S, scorelist):
    """gets score of word given a string"""
    if S == "":
        return 0
    return letterScore(S[0], scorelist) + wordScore(S[1:], scorelist)

#print(wordScore("wow", [['o', 10], ['w', 42]]))

def remove(S, rack):
    """removes only one instance of a letter in a rack"""
    if rack == []:
        return []
    if S == rack[0]:
        return rack[1:]
    return [rack[0]] + remove(S, rack[1:])

#print(remove("a", ['a', 'a', 'z', 'd', 'y']))

def isWordPossible(S, rack):
    """returns if word is possible given a rack of letters"""
    if S == "":
        return True
    if S[0] in rack:
        return isWordPossible(S[1:], remove(S[0], rack))
    return False

#print(isWordPossible("hello", ['e', 'p', 'l', 'z', 'o', 'l', 'h']))

def listOfWords(Dictionary, rack):
    """returns a list of words that can work in the rack, mode 1 is with
    the respective scores, mode 2 is without those scores"""
    
    return filter(lambda S: isWordPossible(S, rack), Dictionary)

#print(listOfWords(Dictionary, ['a', 'z', 'b']))

def scoreList(rack, scores):
    """returns the list of possible words with the scores"""
    words = listOfWords(Dictionary, rack)
    return map(lambda S: [S, wordScore(S, scores)], words)

print(scoreList(['a','s','m','o', 'f', 'o'], scrabbleScores))
#print(scoreList(['a', 'b', 'v', 'x', 'y', 'y', 'z', 'z', 'z']))

def bestWord(rack):
    """returns the best word that can be made with the rack (highest value)"""
    possibleWords = scoreList(rack, scrabbleScores)
    def wordHelper(count, index, score):
        if (count == len(possibleWords)):
            return possibleWords[index]
        word = possibleWords[count]
        if word[1] > score:
            return wordHelper(count+1, count, word[1])
        return wordHelper(count+1, index, score)
    return wordHelper(0, 0, 0)

print(bestWord(["a", "s", "m", "t", "p"]))
#print(bestWord(['a','b','m','d']))
#print(bestWord(['a', 'b', 'v', 'x', 'y', 'y', 'z', 'z', 'z']))