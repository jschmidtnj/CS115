'''
Created on Nov 16, 2017

@author: jschmid3@stevens.edu
Pledge:    I pledge my honor that I have abided by the Stevens Honor System -Joshua Schmidt

CS115 - Lab 11
'''
import math
class QuadraticEquation(object):
    '''
    Defines a quadratic equation, in the form
    of ax^2+bx+c=0. It computes the discriminant, finds
    the roots, and can format the equation as a string
    '''
    def __init__(self,a,b,c):
        '''
        constructs a quadratic equation, where a cannot be 0, initialized to the user's
        specified values.
        
        args: ax^2+bx+c=0
        a = coefficient for x^2
        b = coefficient for x
        c = 3rd value
        
        Raises:
        Value Error: if user tries to input 0 for a
        '''
        if a == 0:
            raise ValueError('Coefficient \'a\' cannot be 0 in a quadratic equation.')
        else:
            self.__a = float(a)
        self.__b = float(b)
        self.__c = float(c)
    
    @property
    def a(self):
        '''
        defines a as a
        '''
        return self.__a
    @property
    def b(self):
        '''
        defines b as b
        '''
        return self.__b
    @property
    def c(self):
        '''
        defines c as c
        '''
        return self.__c
    
    def discriminant(self):
        '''
        returns the discriminant (b^2-4ac)
        '''
        return self.__b ** 2 - 4 * self.__a * self.__c
    
    def root1(self):
        '''
        returns root with + in quadratic formula
        '''
        discriminant = self.discriminant()
        if discriminant < 0:
            return None
        return (-1 * self.__b + math.sqrt(discriminant)) / (2 * self.__a)
                
    def root2(self):
        '''
        returns root with - in quadratic formula
        '''
        discriminant = self.discriminant()
        if discriminant < 0:
            return None
        return (-1 * self.__b - math.sqrt(discriminant)) / (2 * self.__a)
                
    def __str__(self):
        '''
        returns the quadratic equation in a nice string
        '''
        if self.__a < 0:
            a_sign = '-'
        else:
            a_sign = ''
        if self.__b < 0 or self.__c < 0:
            b_sign = '-'
        else:
            b_sign = '+'
        if self.__c < 0:
            c_sign = '-'
        else:
            c_sign = '+'
        if self.__a == 1 or self.__a == -1:
            #do not display a
            a = ''
        else:
            a = str(abs(self.__a))
        if self.__b == 0:
            b = ''
        elif self.__b == 1 or self.__b == -1:
            b = b_sign + ' x '
        else:
            b = b_sign + ' ' + str(abs(self.__b)) + 'x '
        if self.__c == 0:
            c = ''
        else:
            c = c_sign + ' ' + str(abs(self.__c)) + ' '
        return a_sign + a + 'x^2 ' + b + c + '= 0'

if __name__ == '__main__':
    '''main function'''
    quad1 = QuadraticEquation(1.2,2.3,5.6)
    print(quad1)
    print(QuadraticEquation.__init__.__doc__) #prints doc string