'''
Created on Nov 21, 2017

@author: jschmidt
'''
from shape import Shape
import math

class Circle(Shape):
    def __init__(self, x, y, radius, name = 'Circle'):
        super().__init__(x, y, name)
        self.__radius = radius
    
    @property
    def radius(self):
        return self.__radius
    
    @radius.setter
    def radius(self, radius):
        self.__radius = radius
    
    #could have been abstractmethod and method, but since this computation
    #is simple - SIMPLE - , you can use property
    @property
    def area(self):
        return math.pi * (self.__radius ** 2)
    
    def __str__(self):
        return super().__str__() + ', radius = ' + \
            str(self.__radius) + ', area = %.3f' % self.area
            #3 decimal places only
            #don't need parenthesis because properties
            #are treated like variables
    
if __name__ == '__main__':
    circle = Circle(20, 20, 5)
    print(circle)