'''
Created on Oct 5, 2017
@author:   jschmid3@stevens.edu
Pledge:    I pledge my honor that I have abided by the Stevens Honor System -Joshua Schmidt

CS115 - Lab 5
'''
import time
from cs115 import map


words = []
HITS = 10

def ED(first, second):
    """ Returns the edit distance between the strings first and second."""
    if first == '':
        return len(second)
    elif second == '':
        return len(first)
    elif first[0] == second[0]:
        return ED(first[1:], second[1:])
    else:
        substitution = 1 + ED(first[1:], second[1:])
        deletion = 1 + ED(first[1:], second)
        insertion = 1 + ED(first, second[1:])
        return min(substitution, deletion, insertion)
    
#print(ED("apples", "mapplees"))
#print(ED("sorry", "Carrie"))
#print(ED("frosted", "frosties"))
#print(ED("makingasdfasdfsdaf", "maps_9123asdfasdfpie"))

def fastED(first, second):
    '''Returns the edit distance between the strings first and second. Uses
    memoization to speed up the process.'''
    def EDMemo(first, second, memo):
        if (first, second) in memo:
            return memo[(first, second)]
        if first == '':
            result = len(second)
        elif second == '':
            result = len(first)
        elif first[0] == second[0]:
            result = EDMemo(first[1:], second[1:], memo)
        else:
            substitution = 1 + EDMemo(first[1:], second[1:], memo)
            deletion = 1 + EDMemo(first[1:], second, memo)
            insertion = 1 + EDMemo(first, second[1:], memo)
            result = min(substitution, deletion, insertion)
        memo[first, second] = result
        return result
    return EDMemo(first, second, {})

#TEST
#print(fastED("makingasdfasdfsdaf", "maps_9123asdfasdfpie"))
#print(fastED("antidisestablishment", "antiquities"))


def getSuggestions(user_input):
    '''For each word in the global words list, determine the edit distance of
    the user_input and the word. Return a list of tuples containing the
    (edit distance, word).
    Hint: Use map and lambda, and it's only one line of code!'''
    return map(lambda i: (fastED(user_input, words[i]), words[i]), range(0, len(words)-1))

def spam():
    '''Main loop for the program that prompts the user for words to check.
    If the spelling is correct, it tells the user so. Otherwise, it provides up
    to HITS suggestions.

    To exit the loop, just hit Enter at the prompt.'''
    while True:
        user_input = input('spell check> ').strip()
        if user_input == '':
            break
        if user_input in words:
            print('Correct')
        else:
            start_time = time.time()
            suggestions = getSuggestions(user_input)
            suggestions.sort()
            endTime = time.time()
            print('Suggested alternatives:')
            for suggestion in suggestions[:HITS]:
                print(' %s' % suggestion[1])
            print('Computation time:', endTime - start_time, 'seconds')
    print('Bye')

if __name__ == '__main__':
    f = open('3esl.txt')
    for word in f:
        words.append(word.strip())
    f.close()
    spam()
