'''
Created on Nov 9, 2017

@author: jschm
'''
def num_matches(list1, list2):
    """returns the number of elements that the
    2 lists have in common"""
    list1.sort()
    list2.sort()
    matches = i = j = 0
    lenLst1 = len(list1)
    lenLst2 = len(list2)
    while i < lenLst1 and j < lenLst2:
        if list1[i] < list2[j]:
            i+=1
        elif list1[i] > list2[j]:
            j+=1
        else: #they are the same
            matches+=1
            i+=1
            j+=1
    return matches

A = ['b', 'd', 'e']
B = ['a', 'b', 'c', 'd']
print(num_matches(A, B))

def keep_matches(list1, list2):
    """returns a list of the elements that
    the two lists have in common"""
    list1.sort()
    list2.sort()
    matches = []
    i = j = count = 0
    lenLst1 = len(list1)
    lenLst2 = len(list2)
    while i < lenLst1 and j < lenLst2:
        if list1[i] < list2[j]:
            i+=1
        elif list1[i] > list2[j]:
            j+=1
        else: #they are the same
            matches.append(list1[i])
            count+=1
            i+=1
            j+=1
    return count, matches

print(keep_matches(A, B))

def drop_matches(list1, list2):
    """returns a list of the elements that are
    not in common"""
    list1.sort()
    list2.sort()
    matches = []
    i = j = 0
    lenLst1 = len(list1)
    lenLst2 = len(list2)
    while i < lenLst1 and j < lenLst2:
        if list1[i] < list2[j]:
            matches.append(list1[i])
            i+=1
        elif list1[i] > list2[j]:
            matches.append(list2[j])
            j+=1
        else: #they are the same
            i+=1
            j+=1
    while i < lenLst1:
        matches.append(list1[i])
        i+=1
    while j < lenLst2:
        matches.append(list2[j])
        j+=1
    return len(matches), matches

print(drop_matches(A, B))

def binary_search(lst, key):
    """searches the list for the key. if the key is present,
    the function returns the index of the key. Otherwise it returns
    -low-1. The list must be sorted"""
    lst.sort()
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = low + (high - low) //2
        if lst[mid] == key:
            return mid
        if lst[mid] < key:
            low = mid + 1
        else:
            hihg = mid - 1
    return -low - 1

lst = [2,12,30,90]
key = 30
print(binary_search(lst, key))