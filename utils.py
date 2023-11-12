#from visual import Game

import numpy as np

def make_shadow(matrice):
    for i in range(len(matrice[0])):
        trig = 0
        for j in range(len(matrice)):
            if matrice[j][i] == 2:
                trig = 1
            if trig == 1 and matrice[j][i] != 2:
                matrice[j][i] = 1
    return matrice

def is_full(line):
    return all(val == 2 for val in line)

def points_line_cleared(matrix):
    points = 0
    for line in matrix:
      if not is_full(line):
        points += 300
        #print("LINE CLEARED BONUS")
    return (points)

def clear(board):
    y = len(board)
    x = len(board[0])
    cleared_board = []
    for index, line in enumerate(board):
        if not is_full(line):
            cleared_board.append(line)
    while len(cleared_board) < y:
        cleared_board.insert(0, [0 for _ in range(x)])
    return cleared_board

def clearlist(board_list):
    for i in range(len(board_list)):
        board_list[i] = clear(board_list[i])

def comparer_matrices(matrice1, matrice2):
    if len(matrice1) != len(matrice2) or len(matrice1[0]) != len(matrice2[0]):
        return False
    for i in range(len(matrice1)):
        for j in range(len(matrice1[0])):
            if matrice1[i][j] != matrice2[i][j]:
                return False
    return True

# def change_ones_to_zeros(matrice):
#     for i in range(len(matrice)):
#         for j in range(len(matrice[0])):
#             if matrice[i][j] == 1:
#                 matrice[i][j] = 0
#     return matrice

def only_zeros_and_twos(matrice):
    for i in range(len(matrice)):
        for j in range(len(matrice[0])):
            if matrice[i][j] != 0 and matrice[i][j] != 2 and matrice[i][j] != 1:
                return False
    return True

def substract_matrice(matrice1, matrice2):
    ret_matrice = []
    for i in range(len(matrice1)):
        row = []
        for j in range(len(matrice1[0])):
            row.append(matrice1[i][j] - matrice2[i][j])
        ret_matrice.append(row)
    return ret_matrice

def test1():
    test = [[0,0,2,0], \
             [2,2,2,2], \
             [1,1,1,1]]
    clear(test)
    assert(test == 
           [[0,0,0,0], \
            [0,0,2,0], \
            [0,0,1,0]])

def test2():
    test = [[2,2,2,2], \
            [2,2,2,2], \
            [2,2,2,2]]
    clear(test)
    assert(test == 
           [[0,0,0,0], \
            [0,0,0,0], \
            [0,0,0,0]])

def test3():
    test = [[2,2,2,2], \
            [1,1,1,1], \
            [1,1,1,1]]
    clear(test)
    assert(test == 
           [[0,0,0,0], \
            [0,0,0,0], \
            [0,0,0,0]])

def test4():
    test = [[0,2,2,2], \
            [0,1,1,1], \
            [0,1,1,1]]
    clear(test)
    assert(test == 
           [[0,2,2,2], \
            [0,1,1,1], \
            [0,1,1,1]])
def test5():
    test = [[2,2,2,0], \
            [0,1,1,1], \
            [0,1,1,1]]
    clear(test)
    assert(test == 
           [[2,2,2,0], \
            [0,1,1,1], \
            [0,1,1,1]])  
 
def clear_tests():
    print("Launching Tests")
    test1()
    test2()
    test3()
    test4()
    test5()
    print("Success")
if (__name__ == "__main__"):
    clear_tests()