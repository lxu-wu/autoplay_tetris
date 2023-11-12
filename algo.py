# -*- coding: utf-8 -*-
import time
import copy
from utils import *

HAUTEUR_MUL = 1
OMBRE_MUL = 2
TROUS_MUL = 3

J = [[2,0,0],\
     [2,2,2]]

L = [[0,0,2],\
     [2,2,2]]

O = [[2,2],\
     [2,2]]

S = [[0,2,2],\
     [2,2,0]]

Z = [[2,2,0],\
     [0,2,2]]

T = [[0,2,0],\
     [2,2,2]]

I = [[2,2,2,2]]

class algo:
    
    matrice = None
    curr = None
    next = None
    tmpPossible = []
    possibilities = []
    possibilities_first = []
    possibilities_second = []
    possibilities_first_save = []
    possibilities_second_save = []

    
    def __init__(self, curr, next, matrice):
        self.curr = curr
        self.next = next
        self.matrice = matrice


    def place_piece_and_create_list(self):
        self.place_piece_on_piece_all_rotate(self.curr, self.matrice)
        self.possibilities_first = self.possibilities
        self.possibilities_first_save = copy.deepcopy(self.possibilities_first)
        self.possibilities = []
        clearlist(self.possibilities_first)
        for matrice in self.possibilities_first:
            self.place_piece_on_piece_all_rotate(self.next, matrice)
            self.possibilities_second += self.possibilities
            self.possibilities = []
        self.possibilities_second_save = copy.deepcopy(self.possibilities_second)
        clearlist(self.possibilities_second)


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
                        if piece[yPiece][xPiece] == 2  and matrice[y + yPiece][x + xPiece] != 2 :
                            self.place_one_pixel(x + xPiece, y + yPiece, matrice)
                        elif piece[yPiece][xPiece] == 2  and matrice[y + yPiece][x + xPiece] == 2 :
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
                if piece[i][j] == 2 and matrice[y + i][x + j] == 2:
                    return 0
        return 1

    def check_downable(self, x, y, PHauteur, PLargeur, piece, matrice):
        i = y + 1
        hauteur = len(matrice)
        while i < hauteur:
            for j in range(PLargeur):
                if matrice[i][x + j] == 2:
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
            if (matrice[y][x + i] == 0):
                overShadow += 1
            elif matrice[y][x + i] == 1:
                overShadow = 0
            elif matrice[y][x + i] == 2:
                overShadow = 0
            if overShadow >= PLargeur:
                return 1
            i += 1
        return 0


    def place_one_pixel(self, x, y, matrice):
        Hauteur = len(matrice)
        # print(Hauteur, y)
        matrice[y][x] = 2

        for i in range(y + 1, Hauteur):
            if matrice[i][x] == 0:
                matrice[i][x] = 1
    
    def rotate_piece(self, piece):
        piece_pivotee = [[piece[j][i] for j in range(len(piece))] for i in range(len(piece[0])-1, -1, -1)]
        return piece_pivotee
    
    def send_best_map(self):
        best_map = self.choose_best_map()

        for matrice in self.possibilities_first_save:
            substract = substract_matrice(self.possibilities_second_save[best_map[2]], matrice)
            if only_zeros_and_twos(substract):
                return matrice


    def choose_best_map(self):

        best_map = (None, None, None)

        for i in range(len(self.possibilities_second)):
            score = self.scoring(self.possibilities_second[i])
            if score < best_map[1]:
                best_map = (self.possibilities_second[i], score, i)
        
        return best_map

    
    def scoring(self, matrice):
        somme_hauteur = self.nombres_de_un(matrice)
        trous = self.valeurs_des_trous(matrice)
        ombre = self.ombre(matrice)

        sumTrous = sum(trous)

        score = somme_hauteur * HAUTEUR_MUL + sum(trous) * TROUS_MUL + (ombre - sumTrous) * OMBRE_MUL
        return score

    def nombres_de_un(self, matrice):
        somme_de_1=0
        for rangees in (matrice):
            for case in (rangees):
                if case==1: #je check si la case est un 1 (vide mais avec une case remplie juste au dessus)
                    somme_de_1+=1 

        return somme_de_1

    def valeurs_des_trous(self, matrice):
        # fonction pour check si un 1 touche un 0
        def touche_0(i, j):
            if i > 0 and matrice[i - 1][j] == 0 or i < len(matrice) - 1 and matrice[i + 1][j] == 0 or j > 0 and matrice[i][j - 1] == 0 or j < len(matrice[i]) - 1 and matrice[i][j + 1] == 0:
                return True
            
        flag=True
        while flag: #j'itere le temps qu'il y ai plus de 0 qui touchent de 1
            flag = False  
            for i in range(len(matrice)):
                for j in range(len(matrice[i])):
                    if matrice[i][j] == 1 and touche_0(i, j):
                        matrice[i][j] = 0
                        flag = True

        trous = []
        index_cases = []

        for i in range(len(matrice)):
            for j in range(len(matrice[i])):
                if matrice[i][j] == 1 and (i, j) not in index_cases:
                    nombre_case_trou = 0
                    queue = [(i, j)]
                    index_cases.append((i, j))

                    while queue:
                        current_i, current_j = queue[0]
                        nombre_case_trou += 1
                        queue=[]

                        # je check la case en haut
                        if current_i > 0 and matrice[current_i - 1][current_j] == 1 and (current_i - 1, current_j) not in index_cases:
                            queue.append((current_i - 1, current_j))
                            index_cases.append((current_i - 1, current_j))

                        # check la case en dessous
                        if current_i < len(matrice) - 1 and matrice[current_i + 1][current_j] == 1 and (current_i + 1, current_j) not in index_cases:
                            queue.append((current_i + 1, current_j))
                            index_cases.append((current_i + 1, current_j))

                        # check la case à gauche
                        if current_j > 0 and matrice[current_i][current_j - 1] == 1 and (current_i, current_j - 1) not in index_cases:
                            queue.append((current_i, current_j - 1))
                            index_cases.append((current_i, current_j - 1))

                        # check la case à droite
                        if current_j < len(matrice[i]) - 1 and matrice[current_i][current_j + 1] == 1 and (current_i, current_j + 1) not in index_cases:
                            queue.append((current_i, current_j + 1))
                            index_cases.append((current_i, current_j + 1))
                        

                    trous.append(nombre_case_trou)

        return trous

    def somme_hauteurs(self, matrice):
        somme=0
        for num_rows in range(len(matrice)):
            for num_columns in range(len(matrice[0])):
                if matrice[num_rows][num_columns]==2: #je check si la case est remplie ou pas
                    somme+=len(matrice)-num_rows #comme on commence par le haut il faut faire 21-la rangée

        return somme

# Hauteur = 10
# Largeur = 4
# matrice_grande = [[0  for _ in range(Largeur)] for _ in range(Hauteur)]

# # for i in matrice_grande:
# #     print(i)

# # for i in matrice_grande:
# #     print(i, end='\n')
# # print('')

# al = algo(T, I, matrice_grande)
# al.place_one_pixel(0, 4, al.matrice)
# al.place_one_pixel(1, 4, al.matrice)
# al.place_piece_and_create_list()

# for a in al.possibilities_second:
#     for i in a:
#         print(i)
#     print('')
# #     # break

# print(len(al.possibilities_second))

# for m1 in al.possibilities_second:
#     for m2 in al.possibilities_second:
#         if m1 != m2:
#             if comparer_matrices(m1, m2):
#                 print(m1)
#                 print(m2)
    


