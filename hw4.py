'''
Created on Oct 4, 2017

@author: jschmid3@stevens.edu
Pledge:    I pledge my honor that I have abided by the Stevens Honor System -Joshua Schmidt

CS115 - hw4
'''
def pascal_row(n):
    """returns the pascal triangle row of the given integer n"""
    def triangle(n, lst):
        if lst ==[]:
            lst = [[1]]
        if n == 1:
            return lst
        else:
            oldRow = lst[-1]
            def helpRows(lst1, lst2):
                if lst1 == [] or lst2 == []:
                    return []
                return [(lst1[0], lst2[0])] + helpRows(lst1[1:], lst2[1:])
            def summation(lst):
                if lst == []:
                    return []
                return [sum(lst[0])] + summation(lst[1:])
            newRow = [1] + summation(helpRows(oldRow, oldRow[1:])) + [1]
            return triangle(n - 1, lst + [newRow])
    return triangle(n + 1, [])[n]

def pascal_triangle(n):
    """returns the pascal triangle from 0 to n"""
    def triangle(n, lst):
        if lst ==[]:
            lst = [[1]]
        if n == 1:
            return lst
        else:
            oldRow = lst[-1]
            def helpRows(lst1, lst2):
                if lst1 == [] or lst2 == []:
                    return []
                return [(lst1[0], lst2[0])] + helpRows(lst1[1:], lst2[1:])
            def summation(lst):
                if lst == []:
                    return []
                return [sum(lst[0])] + summation(lst[1:])
            newRow = [1] + summation(helpRows(oldRow, oldRow[1:])) + [1]
            return triangle(n - 1, lst + [newRow])
    return triangle(n + 1, [])


#TESTING
#print(pascal_row(0))
#print(pascal_triangle(3))