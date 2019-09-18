'''
Created on Oct 31, 2017

@author: jschm
'''


def mapSqr(L):
    """returns the map of sqr and L"""
    power = 2
    lst = []
    # have to make a new list so old is not mutated
    # cannot do better
    for x in L:
        #lst += [x ** power]
        # faster
        lst.append(x ** power)
    return lst


print(mapSqr([1, 2, 3, 4, 5]))


def findMax(lst):
    if lst == []:
        return None
    max = lst[0]
    for x in lst:
        if x > max:
            max = x
    return max

# print(findMax([]))
# print(findMax([1,2,6,4,5]))


def find_min_max(lst):
    if lst == []:
        return None
    max = min = lst[0]
    for x in lst:
        if x < min:
            min = x
        elif x > max:
            max = x
    return min, max


print(find_min_max([1, 9, 6, 4, 5]))


def sequential_search(lst, key):
    for i in range(len(lst)):
        if lst[i] is key:
            return i
    return -1


print(sequential_search(["apple", "pear", "orange", "orange"], "orange"))


def shallow_copy(L):
    new_list = []
    for x in L:  # for each loop, because we do not need the index
        new_list.append(x)  # more efficient and concise
    return new_list


"""
L = [1,2,3]
M = shallow_copy(L)
M[2] = 33
print(L)
print(M)

S = [[1,2],[3,4],[5,6]]
T = shallow_copy(S)
T[2][1] = 66
print(S)

S = [[1,2],[3,4],[5,6]]
T = shallow_copy(S)
T[2] = [7,8]
print(S)
"""


def deep_copy(L):
    new_list = []
    for x in L:
        if isinstance(x, list):
            new_list.append(deep_copy(x))
        else:
            new_list.append(x)
    return new_list


S = [[1, 2], [3, 4], [5, 6]]
T = shallow_copy(S)
T[2][0] = 7
print(S)


def create_board(r, c):
    board = []
    for _ in range(r):  # need it to count, so use underscore because we don't need value
        row = []
        for _ in range(c):
            row.append(' ')
        board.append(row)
    return board


board = create_board(3, 3)
print(board)


def create_board_comp(r, c):
    """very short now! - list compression"""
    return [[' ' for _ in range(c)] for _ in range(r)]


board = create_board_comp(3, 3)
board[0][0] = 'X'  # upper character
board[2][2] = 'O'  # bottom right character
print(board)

# NOW MAKE WITH ASCII ART!


def display_board(board):
    num_row = len(board)
    for row in range(num_row):
        num_col = len(board[row])
        for col in range(num_col):
            # can't go to new line right after
            print(' ' + board[row][col] + ' ', end='')
            if col < num_col - 1:
                print('|', end='')
        print()
        if row < num_row - 1:
            print('-' * (num_col * 4 - 1))


board = create_board_comp(3, 3)
board[0][0] = 'X'  # upper character
board[2][2] = 'O'  # bottom right character
display_board(board)


"""
def find_max_2D(L):
    #with max of each subset
    result = []
    for x in range(len(L)):
        max = L[x][0]
        for y in range(len(L[x])):
            if L[x][y] > max:
                max = L[x][y]
        result+=[max]
    return result
"""


def find_max_2D(L):
    max = L[0][0]
    for row in L:
        for x in row:
            if x > max:
                max = x
    return max


ragged = [[1, 10, 9, 6], [3], [4, 12, 17, 1, 13], [8, 7]]
print(find_max_2D(ragged))


def find_max_2D_coords(L):
    rowIN = columnIN = 0
    max = L[0][0]
    for r in range(len(L)):
        for c in range(len(L[r])):
            if L[r][c] > max:
                max = L[r][c]
                rowIN = r
                columnIN = c
    return columnIN, rowIN


print(find_max_2D_coords(ragged))


def swap(lst, a, b):
    temp = lst[a]
    lst[a] = lst[b]
    lst[b] = temp


def selection_sort(L):
    n = len(L)
    for i in range(n-1):
        min_index = i
        for j in range(i + 1, n):
            if L[j] < L[min_index]:
                min_index = j
        if i != min_index:
            swap(L, i, min_index)


def selection_sort_rec(L):
    min_index = 0
    for i in range(1, len(L)):
        if L[i] < L[min_index]:
            min_index = i
    if min_index != 0:
        swap(L, 0, min_index)
    selection_sort_rec(L[1:])


def TowerOfHanoi(n, from_rod, to_rod, aux_rod):
    if n == 1:
        print("Move disk 1 from rod", from_rod, "to rod", to_rod)
        return
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
    print("Move disk", n, "from rod", from_rod, "to rod", to_rod)
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)


L = [3, 2, 5, 1, 4, 6]
selection_sort(L)
print(L)
TowerOfHanoi(4, 'A', 'C', 'B')
