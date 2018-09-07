'''
Created on Sep 28, 2017

@author: jschmid3@stevens.edu
Pledge:    I pledge my honor that I have abided by the Stevens Honor System -Joshua Schmidt

CS115 - Lab4
'''
def knapsack(capacity, itemList):
    """I am now a thief, and need to steal the most
    valuable stuff possible. itemList = [[item1weight, item1val], [item2weight, item2val]]
    etc. Capacity is amount of weight possible. 
    """
    if capacity == 0:
        return [0, []]
    if itemList == []:
        return[0, []]
    item = itemList[0]
    weight = item[0]
    if weight > capacity:
        return knapsack(capacity, itemList[1:])
    value = item[1]
    result = knapsack(capacity - weight, itemList[1:])
    use_it = [value + result[0], [itemList[0]] + result[1]]
    lose_it = knapsack(capacity, itemList[1:])

    if use_it[0] > lose_it[0]:
        return use_it
    return lose_it

#print(knapsack(8, [[36, 35], [10, 28], [39, 47], [8, 1], [7, 24]]))
#sum_use_it = reduce(lambda x, y: x + y, (lambda a, b: [((use_it[1])[a])[1]] + [((use_it[1])[b])[1]]))