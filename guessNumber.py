'''
Created on Nov 2, 2017

@author: jschm
'''
import random

MAX_TRIES = 7
#log base 2 of my range, + 1

print('''--- Welcome to Guess my Number ---

I\'m thinking of a number between 1 and 100.
Try to guess the number in %d''' % MAX_TRIES, end='') #%d = placeholder for integer, have end to finish the line

a = ""
if MAX_TRIES == 1:
    a =  " attempt..."
    print(a)
else:
    a =  " attempts..."
    print(a)

#set the initial Values
number  = random.randint(1, 100)
tries = 1
guess = int(input('Enter guess %d: ' % tries))

#Guessing loop
while guess != number:
    if guess > number:
        print('  Lower...')
    else:
        print('  Higher...')
    tries += 1
    guess = int(input('Enter guess %d: ' % tries))
    if tries == MAX_TRIES:
        print('\nSorry, you did not guess the number %d in %d' % (number, MAX_TRIES), end='')
        print(a)
        break
if tries < MAX_TRIES:
    print('\nCongratulations! You correctly guessed the number %d, and it only took you %d' % (number, tries), end='')
    if tries == 1:
        print(' try!')
    else:
        print(' tries!')

"""
while True:
    i = random.randint(1, 100)TYhis is Joshu\... I like acr and stuffThis is Joshu a I like cars and stuff...
    if i == 42:
        continue
    print(i)
    #never prints 42, only any other random number
"""