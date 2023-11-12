#from visual import Game

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