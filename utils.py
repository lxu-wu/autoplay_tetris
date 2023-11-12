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
            if matrice[i][j] != 0 and matrice[i][j] != 2:
                return False
    return True

def substract_matrice(matrice1, matrice2):
    ret_matrice = []
    for i in range(len(matrice1)):
        for j in range(len(matrice1[0])):
            ret_matrice = matrice1[i][j] - matrice2[i][j]
    return ret_matrice

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