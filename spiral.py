'''
Created on Oct 5, 2017

@author: jschm
'''
import turtle

#distance - length of current wall
#initial - length of first wall on the inner past of the spiral
def square_spiral(walls):
    def square_spiral_helper(distance, initial, count):
        if count == walls:
            turtle.done()
        else:
            turtle.left(90)
            turtle.forward(distance)
            square_spiral_helper(distance + initial * (count%2), initial, count + 1)
            #mod 2 so that every two sides are the same length (gets a square shape)
    square_spiral_helper(20, 20, 0)
    
#square_spiral(30)

def octoganal_spiral(walls):
    def octoganal_spiral_helper(distance, initial, count):
        if count == walls:
            turtle.done()
        else:
            turtle.left(45)
            turtle.forward(distance)
            octoganal_spiral_helper(distance + initial * (count%2), initial, count + 1)
            #mod 2 so that every two sides are the same length (gets a square shape)
    octoganal_spiral_helper(20, 5, 0)
    
octoganal_spiral(30)