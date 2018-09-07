'''
Created on Sep 15, 2017

@author: jschm
'''

def deepReverse(L):
    """reverses order of list"""
    def reverseHelp(L, lst, c):
        if(L == []):
            return lst
        if(isinstance(L[c], list)):
            #if(isinstance(L[1], list)==False):   
            return reverseHelp(L[0], lst, 0)
        else:
            return reverseHelp(L[c:], [L[c]]+lst, c+1)
    return reverseHelp(L, [], 0)

print(deepReverse([1, [2, [3, 4], [5, [6, 7], 8]]]))