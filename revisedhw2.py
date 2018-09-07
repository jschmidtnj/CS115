'''
Created on 9/16/17
@author:   jschmid3@stevens.edu
Pledge:    I pledge my honor that I have abided by the Stevens Honor System -Joshua Schmidt

CS115 - Hw 2
'''
import sys
from cs115 import map, reduce, filter
from bigdict import *
# Be sure to submit hw2.py.  Remove the '_template' from the file name.

# Allows up to 10000 recursive calls.
# The maximum permitted limit varies from system to system.
sys.setrecursionlimit(10000)
#sys.setrecursionlimit(1999999999)

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
    for x in scorelist:
        if(letter == x[0]):
            return x[1]
    return 0

print(letterScore('y', scrabbleScores))

def explode(s):
    """returns a string, but as a list, with one
    character per index"""
    def explodeHelp(s, accum):
        if(s==""):
            return accum
        return explodeHelp(s[1:], accum + [s[0]])
    return explodeHelp(s,[])

print(explode("apple"))

def letterPoints(rack, scorelist):
    if rack == "":
        return 1
    return letterScore(rack[0], scorelist) * letterScore(rack[1:], scorelist)
    
print(letterPoints('l', scrabbleScores))

def isWordPossible(S, rack):
    """returns if word is possible given a rack of letters"""
    if S == "":
        return True
    if S[0] in rack:
        return isWordPossible(S[1:], remove(S[0], rack))
    return False

def remove(S, rack):
    """removes only one instance of a letter in a rack"""
    if rack == []:
        return []
    if S == rack[0]:
        return rack[1:]
    return [rack[0]] + remove(S, rack[1:])
    
def listOfWords(rack):
    """returns a list of words that can work in the rack, mode 1 is with
    the respective scores, mode 2 is without those scores"""
    return filter

def scoreList(rack):
    """returns the list of possible words with the scores"""
    return listOfWords(rack, 1)

print(scoreList(['a','b','m','d']))

def bestWord(Rack):
    """returns the best word that can be made with the rack (highest value)"""
    if(Rack == []):
        return []
    words = listOfWords(Rack, 2)
    def wordHelp(words, current, index, highValue):
        if(index == len(words)-1):
            return [words[index]] + [wordScore(words[index], scrabbleScores)]
        if(wordScore(words[current], scrabbleScores) > highValue):
            highValue = wordScore(words[index], scrabbleScores)
            #print(highValue)
            index = current
        return wordHelp(words, current + 1, index, highValue)
    return wordHelp(words, 0, 0, 0)

print(bestWord(['a','b','m','d']))
print(bestWord(["a", "s", "m", "t", "p"]))
print(bestWord(['a', 'b', 'v', 'x', 'y', 'y', 'z', 'z', 'z']))
"""
def combos(lst, numChar):
    newlst = []
    for i in range(numChar):
        #newlst.append(0)
        newlst = newlst + [0]
    return getCombos(lst, 0, newlst, 0, numChar)

def getCombos(lst, index, combo, indexCombo, numChar):
    if indexCombo == numChar:
        return [combo[:]]
    if index >= len(lst):
        return []
    combo[indexCombo] = lst[index]
    
    return getCombos(lst, index + 1, combo, indexCombo + 1, numChar) + getCombos(lst, index + 1, combo, indexCombo, numChar)
print(combos([1,2,3,4], 2))
"""

"""
def combos(lst, numChar):
    def comboHelp(lst, numChar, count, accum):
        
        return(lst, numChar, count+1, accum + lst[count])

def scoreList(Rack):
    if len(Rack) <= 1:
        return [Rack[0]] +  [wordScore(Rack[0], scrabbleScores)]
"""
"""
def allpermutationsOfString(words):
  if len(words) == 1:
    return [words]
  result = []
  for index, letter in enumerate(words):
    wordWithoutLetter = words[:index] + words[index+1:]
    result = result + [letter + word for word in allpermutationsOfString(wordWithoutLetter)]
  return result

print allpermutationsOfString("watup") #will print all permutations of watup
"""