'''
Created on Feb 10, 2015
Last modified on Jan 23, 2016

@author: Brian Borowski

CS 115 - Using lambda
'''
from cs115 import map, filter

# We will use this list of names.
list_of_names = ['Abe', 'Barry', 'Christine', 'Dean', 'Emma', 'Frank']

def names_and_lengths(list_of_names):
    '''Returns a list of [name, length] pairs.
    Notice how map operates on a list of names. We can use lambda to take in
    one argument -- a single name and return a [name, length] pair.'''
    return map(lambda name: [name, len(name)], list_of_names)

def filter_names(name_length_pairs, min_length):
    '''Returns a list of all [name, length] pairs where the length field is
    >= min_length.

    For instance, assuming list_of names starts off as the list in line 10 and
    min_length is 5, the list returned by this function will
    include only [['Barry', 5], ['Christine', 9], ['Frank', 5]].

    lambda takes in a single pair from name_length_pairs, for example,
    ['Abe', 3].
      - pair[0] is 'Abe'
      - pair[1] is 3'''
    return filter(lambda pair: pair[1] >= min_length, name_length_pairs)

name_length_pairs = names_and_lengths(list_of_names)
print(name_length_pairs)

long_names = filter_names(name_length_pairs, 5)
print(long_names)
