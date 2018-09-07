'''
Created on Nov 9, 2017

@author: jschmid3@stevens.edu
Pledge:    I pledge my honor that I have abided by the Stevens Honor System -Joshua Schmidt

CS115 - Lab 10
'''
import random
import sys
from pip._vendor.html5lib._inputstream import spacesAngleBrackets
from random import randint

def createOneRow(width):
    """Returns one row of zeros of width "width"...  
       You should use this in your
       createBoard(width, height) function."""
    row = []
    for col in range(width):
        row += [0]
    return row

def createBoard(width, height):
    result = []
    for row in range(height):
        firstRow = []
        for col in range(width):
            firstRow += [0]
        result+=[firstRow]
    return result

#print(createBoard(5, 3))

def printBoard(A):
    """this function prints the 2d list
    of lists without spaces, using sys.
    stdout.write()
    """
    for row in A:
        for col in row:
            sys.stdout.write(str(col))
        sys.stdout.write('\n')
        
#A = createBoard(5,3)
#printBoard(A)

def diagonalize(width, height):
    """creates an empty board and then modifies
    if so that it has a diagonal strip of 'on' cells"""
    A = createBoard(width, height)
    for row in range(height):
        for col in range(width):
            if row == col:
                A[row][col] = 1
            else:
                A[row][col] = 0
    return A

#A = diagonalize(7,6)
#print(A)
#printBoard(A)

def innerCells(w,h):
    A = createBoard(w,h)
    for row in range(h):
        for col in range(w):
            if (row != 0 and row != h-1) and (col != 0 and col != w-1):
                A[row][col] = 1
    return A

#A = innerCells(5,5)
#printBoard(A)

def randomCells(w,h):
    """returns an array of randomly-assigned
    1s and 0s except the outer edge is all 0s"""
    A = innerCells(w, h)
    for row in range(h):
        for col in range(w):
            if A[row][col] == 1:
                A[row][col] = random.choice([0,1])
    return A

#A = randomCells(10,10)
#printBoard(A)

def copy(A):
    copy = []
    for row in range(len(A)):
        newRow = []
        for col in range(len(A[row])):
            newRow.append(A[row][col])
        copy.append(newRow)
    return copy

"""
oldA = createBoard(2,2)
printBoard(oldA)
newA = copy(oldA)
printBoard(newA)
oldA[0][0]=1
printBoard(oldA)
printBoard(newA)
if oldA != newA:
    print("works")
else:
    print("doesn't work")
"""

def innerReverse(A):
    result = copy(A)
    h = len(result)
    w = len(result[0])
    for row in range(h):
        for col in range(w):
            if  (row == 0 or row == h-1) or (col == 0 or col == w-1):
                result[row][col] = 0
            elif result[row][col] == 1:
                result[row][col] = 0
            else:
                result[row][col] = 1
    return result

"""
A = randomCells(8, 8)
printBoard(A)
print("\n\n")pyth
A2 = innerReverse(A)
printBoard(A2)
"""

def numNeighbors(A, r, c):
    """finds the number of neighbors of coordinate r,c in board A"""
    count = 0
    for row in range(r-1, r+2):
        for col in range(c-1, c+2):
            if not(row == r and col == c) and A[row][col] == 1:
                count+=1
    return count

"""
A = randomCells(8,8)
printBoard(A)
print(numNeighbors(A, 3, 4))
"""

def next_life_generation(A):
    """makes a copy of A and then advances
    one generation of Conway's game of life
    within the inner cells of that copy. the
    outer edge always stays 0
    """
    newA = copy(A)
    h = len(newA)
    w = len(newA[0])
    for row in range(h):
        for col in range(w):
            if  (row == 0 or row == h-1) or (col == 0 or col == w-1):
                newA[row][col] = 0
            elif numNeighbors(A, row, col) < 2:
                newA[row][col] = 0
            elif numNeighbors(A, row, col) > 3:
                newA[row][col] = 1
            elif numNeighbors(A, row, col) == 3 and newA[row][col] == 0:
                newA[row][col] = 1
    return newA

A = [ [0,0,0,0,0],
 [0,0,1,0,0],
 [0,0,1,0,0],
 [0,0,1,0,0],
 [0,0,0,0,0]]
printBoard(A)
print()
A2 = next_life_generation(A)
printBoard(A2)
print("\n")
A3 = next_life_generation(A2)
printBoard(A3)

