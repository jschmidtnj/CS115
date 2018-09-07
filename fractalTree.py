'''
Created on Oct 11, 2017

@author: jschm
'''
import turtle
turtle = turtle.Turtle()

def goodTree(length, level):
    angle = 17
    width = 4
    turtle.width(width)
    turtle.left(90)
    turtle.forward(length)
    def treeHelp(length, level):
        width = turtle.width() #saves current width

        turtle.width(3 / 4 * width)
    
        length = length * 3 / 4
    
        turtle.left(angle)
        turtle.forward(length)
    
        if level < width:
            treeHelp(length * 3 / 4, level + 1)
        turtle.backward(length)
        turtle.right(2 * angle)
        turtle.forward(length)
    
        #do again
        if level < width:
            treeHelp(length * 3 / 4, level + 1)
        turtle.backward(length)
        turtle.left(angle)
    
        turtle.width(width) #same width as before
    treeHelp(length, 6-level) #do not know why this number is weird
goodTree(120, 4)