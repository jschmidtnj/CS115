'''
Created on Oct 3, 2017

@author: jschm
'''

"""
def pascal_row(n):
    def rowHelper(n, count, multiplier, accum):
        if n == count - 1:
            return accum
        if count == 0 or n == count:
            return [1] + rowHelper(n, count + 1, multiplier, accum)
        if count >= (n / 2):
            print(multiplier)
            return [(multiplier-1) * n] + rowHelper(n, count + 1, multiplier - 1, accum)
        return [multiplier * n] + rowHelper(n, count + 1, multiplier + 1, accum)
    return rowHelper(n, 0, 1, [])

print(pascal_row(4))
"""
"""
def pascal_row(n):
    def rowHelper(n, count, accum):
        if n == count - 1:
            return accum
        def createRow(c, lst):
            if len(accum) == 0:
                return [1]
            if len(accum[0]) >= 2:
                return 
    return rowHelper(n, count, [])

print(pascal_row(4))
"""
"""
def pascal_row(n):
    if n == 0:
        return []
    elif n == 1:
        return [[1]]
    else:
        newRow = [1]
        rows = pascal_row(n-1)
        lastRow = rows[len(rows)-1]
        print(lastRow)
        print(lastRow)
        def rowHelper(c):
            if c == len(lastRow) - 1:
                return newRow.append([1])
            return newRow.append(lastRow[c] + lastRow[c+1])
        newRow = rowHelper(0)
        print(newRow)
        rows.append(newRow)
    return rows

print(pascal_row(3))

"""


def pascal_row(n):

    def helpRows(lst1, lst2):
        if lst1 == [] or lst2 == []:
            return []
        return [(lst1[0], lst2[0])] + helpRows(lst1[1:], lst2[1:])

    def summation(lst):
        if lst == []:
            return []
        return [sum(lst[0])] + summation(lst[1:])

    def triangle(n, lst):
        if lst == []:
            lst = [[1]]
        if n == 1:
            return lst
        else:
            oldRow = lst[-1]
            newRow = [1] + summation(helpRows(oldRow, oldRow[1:])) + [1]
            return triangle(n - 1, lst + [newRow])

    return triangle(n + 1, [])

if __name__ == "__main__":
    print(pascal_row(5))
