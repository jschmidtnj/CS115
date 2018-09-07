



import sys
from cs115 import *

sys.setrecursionlimit(10000)

Dictionary = ['902', '820', '888', '270', '999', '123', '456', '789', '209', 
              '884', '423', '723', '210']

bonglePoints = \
[ ['0', 1.2], ['1', 3.3], ['2', 3.1],['3', 2.5], ['4', 1.0], ['5', 4.9], ['6', 2.8],
 ['7', 4.2], ['8', 1.1], ['9',8.1 ] ]


def numberPoints(number, pointslist):
    if pointslist ==[]:
        return 0.0
    first = pointslist[0]
    if first[0] == number:
        return first[1]
    return numberPoints(number, pointslist[1:])
print(numberPoints('2', bonglePoints))

def codePoints(code, pointslist):
    if code == "":
        return 1
    return numberPoints(code[0], pointslist) * codePoints(code[1:], pointslist)

print(codePoints('2', bonglePoints))

def remove(number, numbers):
    if numbers == []:
        return []
    if number == numbers[0]:
        return numbers[1:]
    return [numbers[0]] + remove(number, numbers[1:])

def is_code_possible(code, numbers):
    if code == '':
        return True
    if code[0] in numbers:
        return is_code_possible(code[1:], remove(code[0], numbers))
    return False

def list_of_codes_created(Dictionary, numbers):
    return filter(lambda code: is_code_possible(code, numbers), Dictionary)

print(list_of_codes_created(Dictionary, ['9', '8', '5', '4', '6']))

def pointsList(numbers):
    codes = list_of_codes_created(Dictionary, numbers)
    return map(lambda code: [code, codePoints(code, bonglePoints)], codes)

[['456', 12], ['908', 13]]

def bestCode(numbers):
    contenders = pointsList(numbers)
    def better_code(x, y):
        if x[1] > y[1]:
            return reduce(lambda x, y: contenders)
        return y 
    return reduce( y, contenders)
print(bestCode(['1', '2', '3']))

    