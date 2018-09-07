'''
Created on Nov 14, 2017

@author: jschm
'''
class Fraction(object):
    '''Defines an immutable rational number with common arithmetic operations.
    '''

    def __init__(self, numerator=0, denominator=1):
        #default values for fraction is 0
        '''Constructs a rational number (fraction) initialized to zero or a user
        specified value.

        Args:
            numerator: the numerator of the fraction. (Default is 0).
            denominator: the denominator of the fraction (Default is 1).

        Raises:
            ZeroDivisionError: if the user tries to construct a fraction with
            the denominator 0.
        '''

        # The denominator cannot be zero.
        if denominator == 0:
            raise ZeroDivisionError("Denominator cannot be zero.")

        # If the rational number is zero, set the denominator to 1.
        if numerator == 0:
            self.__numerator = 0
            self.__denominator = 1

        # Otherwise, store the rational number in reduced form.
        else:
            # Determine the sign.
            if numerator * denominator < 0:
                sign = -1
            else:
                sign = 1

            # Reduce to smallest form.
            a = abs(numerator)
            b = abs(denominator)
            while a % b != 0:
                temp_a = a
                a = b
                b = temp_a % b
            #b is greatest common divisor
            self.__numerator = abs(numerator) // b * sign
            self.__denominator = abs(denominator) // b

    def __eq__(self, other):
        '''Determines if this fraction is equal to another fraction.

        Args:
            other: the right-hand side fraction

        Returns:
            True if the fractions are equal, False otherwise
        '''
        #don't put any characters after backslash
        return self.__numerator == other.__numerator and \
            self.__denominator == other.__denominator

    def __add__(self, other):
        '''Adds a fraction to this fraction.

        Args:
            other: the right-hand side fraction

        Returns:
            a new Fraction object resulting from the addition
        '''
        num = (self.__numerator * other.__denominator + self.__denominator * other.__numerator)
        den = (self.__denominator * other.__denominator)
        return Fraction(num, den)

    def __sub__(self, other):
        '''Subtracts a fraction from this fraction.

        Args:
            other: the right-hand side fraction

        Returns:
            a new Fraction object resulting from the subtraction
        '''
        num = (self.__numerator * other.__denominator - self.__denominator * other.__numerator)
        den = (self.__denominator * other.__denominator)
        return Fraction(num, den)

    def __mul__(self, other):
        '''Multiplies this fraction by another fraction.

        Args:
            other: the right-hand side fraction

        Returns:
            a new Fraction object resulting from the multiplication
        '''
        num = (self.__numerator * other.__numerator)
        den = (self.__denominator * other.__denominator)
        return Fraction(num, den)

    def __truediv__(self, other):
        #have to use self as first argument
        #one slash, not 2 slashes - __floordiv__
        '''Divides this fraction by another fraction.

        Args:
            other: the right-hand side fraction

        Returns:
            a new Fraction object resulting from the division
        '''
        num = (self.__numerator * other.__denominator)
        den = (self.__denominator * other.__numerator)
        return Fraction(num, den)

    def __lt__(self, other):
        '''Determines if this fraction is less than another fraction.

        Args:
            other: the right-hand side fraction

        Returns:
            True if this fraction is less than the other, False otherwise
        '''
        return self.__numerator * other.__denominator < \
            self.__denominator * other.__numerator

    def __ne__(self, other):
        '''Determines if this fraction is not equal to another fraction.

        Args:
            other: the right-hand side fraction

        Returns:
            True if the fractions are not equal, False otherwise
        '''
        return not self == other

    def __le__(self, other):
        '''Determines if this fraction is less than or equal to another fraction.

        Args:
            other: the right-hand side fraction

        Returns:
            True if this fraction is less than or equal to the other, False
            otherwise
        '''
        return not other < self

    def __gt__(self, other):
        '''Determines if this fraction is greater than another fraction.

        Args:
            other: the right-hand side fraction

        Returns:
            True if this fraction is greater than the other, False otherwise
        '''
        return other < self

    def __ge__(self, other):
        '''Determines if this fraction is greater than or equal to another
        fraction.

        Args:
            other: the right-hand side fraction

        Returns:
            True if this fraction is greater than or equal to the other, False
            otherwise
        '''
        return not self < other

    def __float__(self):
        '''Converts a fraction to a floating-point number.

        Returns:
            the floating-point value of this fraction
        '''
        return float(self.__numerator) / self.__denominator

    def __repr__(self):
        '''Gets an official string representation of the fraction.

        Returns:
            a string in the format Fraction(numerator, denominator)
        '''
        #using name of the class without writing it
        return self.__class__.__name__ + '(' + str(self.__numerator) +',' + str(self.__denominator) + ')'

    def __str__(self):
        '''Gets a user-friendly string representation of the fraction.

        Returns:
            a string in the format numerator/denominator
        '''
        return str(self.__numerator) + '/' + str(self.__denominator)

if __name__ == '__main__':
    f = Fraction(1, 2)
    g = Fraction(4,8)
    print(f,g)
    print(Fraction(1,2) * Fraction(3,5))
    print(Fraction(20,5) / Fraction(2,1))
    print(f == g)
    print(f <= g)
    print(f < g)
    print(f >= g)
    print(f > g)
    h = Fraction(1,3)
    print(repr(h))
    print(h)
    print(float(h))
    print(Fraction.__init__.__doc__) #prints doc string
    lst = [Fraction(2,5), Fraction(1,2), Fraction(1,6), Fraction(1,3)]
    lst.sort() #uses our revised functions
    print(lst)
    
    print(h)
    h._Fraction__numerator = 3
    print(h) #it is not private? code is broken - name mangling (python does not allow for private stuff)
    

"""Encapsulation - within the class, we've enclosed all the member variables and methods
needed to perform the required functionality"""


