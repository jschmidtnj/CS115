'''
Created on Sep 5, 2017

@author: jschm
'''
"""C=5/9*(F-32) F=9/5C+32"""

def fahrenheit(celsius):
    """Returns the input Celcius degrees in Fahrenheit"""
    return 9 / 5 * celsius + 32

def celsius(fahrenheit):
    """Returns the input Celcius degrees in Fahrenheit"""
    return 5 / 9 * (fahrenheit - 32)

"""
Call the functions below the function definitions
input() lets the user input a string and outputs it
"""
c = float(input('enter degrees in Celsius: '))
f = fahrenheit(c)

#you can print multiple items in one statement, If you put a comma after each item, 
#it prints a space and then goes on to print the next item

print(c, 'C = ', f, 'F');
#printing this way gives you 2 decimal places exactly
print('%.2f C = %.2f F' % (c,f))

f = float(input('Enter degrees in Fahrenheit: '))
c = celsius(f)
print(f, 'F = ', c, 'C');
#printing this way gives you 2 decimal places exactly
print('%.2f F = %.2f C' % (f,c))


"""
Try composition of functions.
Converting a Fahrenheit temperature to Celsius and back to Fahrenheit should
give you the original Fahrenheit temperature.
"""

print() #print by itself prints a new line
f = float(input('Enter degrees in Fahrenheit: '))

#user assert to check the return value is equal to the expected Value
assert fahrenheit(celsius(f)) == f #4 if replaced it will fail (AssertionError)
#no output should be produced, unless the assertion fails, which means you
#have an error (either in your code or in your expectation).
