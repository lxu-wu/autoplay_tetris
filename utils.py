#from visual import Game

import numpy as np

def match_pattern(big_matrix, small_matrix):
    # Get the shape of the small matrix
    small_rows, small_cols = small_matrix.shape

    # Get the shape of the big matrix
    big_rows, big_cols = big_matrix.shape

    # Iterate over the big matrix
    for i in range(big_rows - small_rows + 1):
        for j in range(big_cols - small_cols + 1):
            # Extract a sub-matrix from the big matrix
            sub_matrix = big_matrix[i:i+small_rows, j:j+small_cols]

            # Check if the sub-matrix matches the small matrix or any of its rotations
            for _ in range(4):
                if np.array_equal(sub_matrix * small_matrix, small_matrix):
                    print(f"Match found at position ({i}, {j})")
                    break
                small_matrix = np.rot90(small_matrix)  # Rotate the small matrix

def is_full(line):
    for val in line:
        if val != 2:
            return False
    return True

def clear(board):
    y = len(board)
    x = len(board[0])
    for index,line in enumerate(board):
        if is_full(line):
            for i in range (index, y):
                for j in range(0, x):
                    if board[i][j] == 1 and (index == 0 or (index > 0 and board[index - 1][j] != 2)):
                        board[i][j] = 0
            board.remove(board[index])
            board.insert(0,[0 for i in range(x)])

def clearlist(board_list):
    for board in board_list:
        clear(board)

def comparer_matrices(matrice1, matrice2):
    if len(matrice1) != len(matrice2) or len(matrice1[0]) != len(matrice2[0]):
        return False
    for i in range(len(matrice1)):
        for j in range(len(matrice1[0])):
            if matrice1[i][j] != matrice2[i][j]:
                return False
    return True

def change_ones_to_zeros(matrice):
    for i in range(len(matrice)):
        for j in range(len(matrice[0])):
            if matrice[i][j] == 1:
                matrice[i][j] = 0
    return matrice

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