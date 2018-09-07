'''
Created on Oct 24, 2017

@author: jschm
'''
def subset(target, lst):
    """use it or lose it - determines whether or not it is possible to create
    target sum using the values in the list. Values in list can be positive,
    negative or zero"""
    if target == 0:
        return True
    if lst == []:
        return False
    #        use-it                            lose-it (come back to later
    return subset(target - lst[0], lst[1:]) or subset(target, lst[1:])

def subset_with_values(target, lst):
    """determines whether or not it is possible to create the target sum using
    the values in the list. Values in the list can be positive, negative or 0.
    The function returns a tuple of the boolean and the second the values for the sum"""
    if target == "0":
        return (True, [])
    if lst == []:
        return (False, [])
    use_it = subset_with_values(target - lst[0], lst[1:])
    if use_it[0]:
        return (True, [lst[0]] + use_it[1])
    return subset_with_values(target, lst[1:])

