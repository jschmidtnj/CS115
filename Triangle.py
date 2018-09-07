'''
Created on Nov 21, 2017

@author: jschm
'''
from shape import Shape

class Triangle(Shape):
    def __init__(self, x, y, base, height, name = 'Circle'):
        super().__init__(x, y, name)
        self.__base = base
        self.__height = height
    
    @property
    def base(self):
        return self.__base
    
    @base.setter
    def base(self, base):
        self.__base = base
    
    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, height):
        self.__height = height
    
    #could have been abstract method and method, but since this computation
    #is simple - SIMPLE - , you can use property
    @property
    def area(self):
        return .5 * self.__base * self.__height
    
    def __str__(self):
        return super().__str__() + ', base = ' + \
            str(self.__base) + ', height = ' + \
            str(self.__height) + ', area = %.3f' % self.area
            #3 decimal places only
            #don't need parenthesis because properties
            #are treated like variables
    
if __name__ == '__main__':
    triangle = Triangle(20, 20, 5, 10)
    print(triangle)