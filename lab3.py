'''
Created on Sep 22, 2017

@author: jschmid3@stevens.edu
Pledge:    I pledge my honor that I have abided by the Stevens Honor System -Joshua Schmidt

CS115 - Lab3
'''
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
print(change(72, [1, 5, 10, 20, 50, 100]))