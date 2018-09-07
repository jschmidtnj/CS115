'''
Created on 10/11/2017
@author:   jschmid3@stevens.edu
Pledge:    I pledge my honor that I have abided by the Stevens Honor System -Joshua Schmidt

CS115 - Hw5
'''
import turtle  # Needed for graphics
turtle = turtle.Turtle()

# Ignore 'Undefined variable from import' errors in Eclipse.

def sv_tree(trunk_length, levels):
    """creates a tree, with # levels meaning number of Y's in branches"""
    if levels == 0:
        return #escape!
    turtle.forward(trunk_length)
    turtle.left(45)
    sv_tree(trunk_length / 2, levels - 1)
    turtle.right(90)
    sv_tree(trunk_length / 2, levels - 1)
    turtle.left(45)
    turtle.backward(trunk_length)
    return #I don't know if I need this here...

def lucas(n):
    """returns lucas numbers - like Fibonacci"""
    if n == 0:
        return 2
    if n == 1:
        return 1
    return lucas(n-1) + lucas(n-2)
#print(lucas(3))
#print(lucas(9)) #YAY! It works

def fast_lucas(n):
    '''Returns the nth Lucas number using the memoization technique
    shown in class and lab. The Lucas numbers are as follows:
    [2, 1, 3, 4, 7, 11, ...]'''
    def lucasMemo(n, memo):
        if n in memo:
            return memo[n]
        if n == 0:
            result = 2
        elif n == 1:
            result = 1
        else:
            result = lucasMemo(n-1, memo) + lucasMemo(n-2, memo)
        memo[n] = result
        return result
    return lucasMemo(n, {})

def change(amount, coins):
    """determines how many coins you would need to make an amount
    in change returns num of coins needed"""
    if amount == 0:
        return 0
    if coins==[]:
        return float("inf")
    amountUse = amount - coins[0]
    if amountUse < 0:
        return change(amount, coins[1:])
    return min(change(amount, coins[1:]), 1 + change(amountUse, coins))

#print(change(72, [1, 5, 10, 20, 50, 100]))
#print(change(888, [1, 5, 10, 20, 50, 100])) #takes forever!

def fast_change(amount, coins):
    '''Takes an amount and a list of coin denominations as input.
    Returns the number of coins required to total the given amount.
    Use memoization to improve performance.'''
    def fast_change_helper(amount, coins, memo):
        if (amount, coins) in memo:
            return memo[(amount, coins)]
        if amount == 0:
            result = 0
        elif coins == (): #DUH! - tuples = (), not []!
            result = float("inf")
        else:
            amountUse = amount - coins[0]
            if amountUse < 0:
                result = fast_change_helper(amount, coins[1:], memo)
            else:
                result = min(fast_change_helper(amount, coins[1:], memo), 1 + fast_change_helper(amountUse, coins, memo))
        memo[(amount, coins)] = result
        return result
    # Call the helper. Note we converted the list to a tuple.
    return fast_change_helper(amount, tuple(coins), {})

#sv_tree(100,6)
#turtle.clear()
# If you did this correctly, the results should be nearly instantaneous.

def goodTree(length, level):
    '''a better fractal tree with turtle for extra credit'''
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
    
        #do again, but backwards
        if level < width:
            treeHelp(length * 3 / 4, level + 1)
        turtle.backward(length)
        turtle.left(angle)
    
        turtle.width(width) #same width as before
    treeHelp(length, 4-level) #do not know why this number is weird

#goodTree(120, 4)
print("FAST_LUCAS_TEST")
print(fast_lucas(3))  # 4
print(fast_lucas(5))  # 11
print(fast_lucas(9))  # 76
print(fast_lucas(24))  # 103682
print(fast_lucas(40))  # 228826127
print(fast_lucas(50))  # 28143753123 #INSTANT!
#print(tuple([1, 5, 10, 20, 50, 100]))

print("FAST_CHANGE_TEST")
print(fast_change(131, [1, 5, 10, 20, 50, 100]))
print(fast_change(292, [1, 5, 10, 20, 50, 100]))
print(fast_change(673, [1, 5, 10, 20, 50, 100]))
print(fast_change(724, [1, 5, 10, 20, 50, 100]))
print(fast_change(888, [1, 5, 10, 20, 50, 100]))

# Should take a few seconds to draw a sv_tree.
print("TREE_TESTS")
sv_tree(100, 6)
turtle.clear()
goodTree(100,6)
turtle.clear()
print("FINISHED")