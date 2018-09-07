'''
Created on Oct 11, 2017

@author: jschm
'''
import turtle
turtle = turtle.Turtle()

turtle.lt(90)

level1 = 13
precision = 120
angle = 17

turtle.width(level1)

turtle.penup()
turtle.backward(precision)
turtle.pendown()
turtle.forward(precision)

def draw_tree(precision, level):
    width = turtle.width()  # save the current pen width

    turtle.width(width * 3.0 / 4.0)  # narrow the pen width

    precision = precision * 3.0 / 4.0

    turtle.left(angle)
    turtle.forward(precision)

    if level < level1:
        draw_tree(precision, level + 1)
    turtle.backward(precision)
    turtle.right(2 * angle)
    turtle.forward(precision)

    if level < level1:
        draw_tree(precision, level1 + 1)
    turtle.backward(precision)
    turtle.left(angle)

    turtle.width(width)  # restore the previous pen width

turtle.speed("fastest")

draw_tree(precision, 2)

turtle.done()