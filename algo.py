import time
import copy
from utils import comparer_matrices


OVER = 0
UNDER = 1

J = [["🍞",'🤍','🤍'],\
     ["🍞","🍞","🍞"]]

L = [['🤍','🤍',"🍞"],\
     ["🍞","🍞","🍞"]]

O = [["🍞","🍞"],\
     ["🍞","🍞"]]

S = [['🤍',"🍞","🍞"],\
     ["🍞","🍞",'🤍']]

Z = [["🍞","🍞",'🤍'],\
     ['🤍',"🍞","🍞"]]

T = [['🤍',"🍞",'🤍'],\
     ["🍞","🍞","🍞"]]

I = [["🍞","🍞","🍞","🍞"]]

class algo:
    
    matrice = None
    curr = None
    next = None
    tmpPossible = []
    possibilities = []
    possibilities_first = []
    possibilities_second = []

    
    def __init__(self, curr, next, matrice):
        self.curr = curr
        self.next = next
        self.matrice = matrice


    def place_piece_and_create_list(self):
        self.place_piece_on_piece_all_rotate(self.curr, self.matrice)
        self.possibilities_first = self.possibilities
        self.possibilities = []
        for matrice in self.possibilities_first:
            self.place_piece_on_piece_all_rotate(self.next, matrice)
            self.possibilities_second += self.possibilities
            self.possibilities = []


    def place_piece_on_piece_all_rotate(self, piece, matrice):
        
        if comparer_matrices(piece, O):
            r = 1
        elif comparer_matrices(piece, S) or comparer_matrices(piece, Z)\
                or comparer_matrices(piece, I):
            r = 2
        else:
            r = 4

        for i in range(r):
            self.place_piece_on_piece(piece, matrice)
            piece = self.rotate_piece(piece)

    def place_piece_on_piece(self, piece, matrice):
        Largeur = len(matrice[0])

        for x in range(Largeur):
            self.place_one_piece_on_piece(x, piece, matrice)
            self.possibilities += self.tmpPossible
            self.tmpPossible = []

    def place_one_piece_on_piece(self, x, piece, matrice):
        Largeur = len(matrice[0])
        Hauteur = len(matrice)


        for row in range(Hauteur - 1, -1, -1):
             cpMatrice = copy.deepcopy(matrice)
             if self.replace_in_matrice(x, row, piece, cpMatrice):
                self.tmpPossible.append(cpMatrice)
                break
             
    def replace_in_matrice(self, x, y, piece, matrice):
        Largeur = len(piece[0])
        Hauteur = len(piece)


        if len(matrice[0]) - x < Largeur:
            return 0

        try:
            if self.check_can_place_under_shadow(x, y + Hauteur - 1, Hauteur, Largeur, piece, matrice) == 0:
                return 0
            if self.check_playable(x, y, Hauteur, Largeur, piece, matrice) == 0:
                return 0
            y = self.check_downable(x, y, Hauteur, Largeur, piece, matrice)
            # print("y = ", y)
            for yPiece in range(Hauteur)[::-1]:
                for xPiece in range(Largeur):
                    # self.place_one_pixel(x + xPiece, y + yPiece, matrice)
                        if piece[yPiece][xPiece] == "🍞"  and matrice[y + yPiece][x + xPiece] != "🍞" :
                            self.place_one_pixel(x + xPiece, y + yPiece, matrice)
                        elif piece[yPiece][xPiece] == "🍞"  and matrice[y + yPiece][x + xPiece] == "🍞" :
                            return 0
                        # for i in matrice:
                        #     print(i)
                        # print('')
        except :
            return 0
        return 1

    def check_playable(self, x, y, PHauteur, PLargeur, piece, matrice):
        for i in range(PHauteur)[::-1]:
            for j in range(PLargeur):
                if piece[i][j] == "🍞" and matrice[y + i][x + j] == "🍞":
                    return 0
        return 1

    def check_downable(self, x, y, PHauteur, PLargeur, piece, matrice):
        i = y + 1
        hauteur = len(matrice)
        while i < hauteur:
            for j in range(PLargeur):
                if matrice[i][x + j] == "🍞":
                    print('1')
                    return i - PHauteur
            i += 1
        print('2')
        return i - PHauteur

    def check_can_place_under_shadow(self, x, y, PHauteur, PLargeur, piece, matrice):
        i = 0
        overShadow = 0
        largeur = len(matrice[0])
        while i < largeur:
            if (matrice[y][x + i] == '🤍'):
                overShadow += 1
            elif matrice[y][x + i] == 1:
                overShadow = 0
            elif matrice[y][x + i] == "🍞":
                overShadow = 0
            if overShadow >= PLargeur:
                return 1
            i += 1
        return 0


    def place_one_pixel(self, x, y, matrice):
        Hauteur = len(matrice)
        # print(Hauteur, y)
        matrice[y][x] = "🍞"

        for i in range(y + 1, Hauteur):
            if matrice[i][x] == '🤍':
                matrice[i][x] = '🔌'
    
    def rotate_piece(self, piece):
        piece_pivotee = [[piece[j][i] for j in range(len(piece))] for i in range(len(piece[0])-1, -1, -1)]
        return piece_pivotee




Hauteur = 10
Largeur = 4
matrice_grande = [["🤍"  for _ in range(Largeur)] for _ in range(Hauteur)]

# for i in matrice_grande:
#     print(i)

# for i in matrice_grande:
#     print(i, end='\n')
# print('')

al = algo(T, I, matrice_grande)
al.place_one_pixel(0, 4, al.matrice)
al.place_one_pixel(1, 4, al.matrice)
al.place_piece_and_create_list()

for a in al.possibilities_second:
    for i in a:
        print(i)
    print('')
#     # break

print(len(al.possibilities_second))

# for m1 in al.possibilities_second:
#     for m2 in al.possibilities_second:
#         if m1 != m2:
#             if comparer_matrices(m1, m2):
#                 print(m1)
#                 print(m2)
    


