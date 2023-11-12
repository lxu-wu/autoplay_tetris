from visual import Game

def is_full(line):
    for val in line:
        if val != 2:
            return False
    return True

def clear(board):
    #Change to y = 3 and x = 4 for testing
    y = Game.V_SIZE
    x = Game.H_SIZE
    for index,line in enumerate(board):
        if is_full(line):
            for i in range (index, y):
                for j in range(0, x):
                    if board[i][j] == 1 and (index == 0 or (index > 0 and board[index - 1][j] != 2)):
                        board[i][j] = 0
            board.remove(board[index])
            board.insert(0,[0 for i in range(x)])

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