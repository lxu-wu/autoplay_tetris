# -*- coding: utf-8 -*-
import time
import copy
from utils import *
from scoring import *

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

class Algo:
	
	def __init__(self, current, next, matrice):
		
		#Conver letter to matrice of piece
		def letter_to_piece_matrice(letter):
			match letter:
				case ('I'):
					return(I)
				case ('T'):
					return(T)
				case ('J'):
					return(J)
				case ('S') :
					return(S)
				case ('O'):
					return(O)
				case ('L'):
					return(L)
				case _:
					return(Z)

		self.curr = letter_to_piece_matrice(current)
		self.next = letter_to_piece_matrice(next)
		self.matrice = matrice
		self.tmpPossible = []
		self.possibilities = []
		self.possibilities_first = []
		self.possibilities_second = []

	def place_piece_and_create_list(self):
		self.place_piece_on_piece_all_rotate(self.curr, self.matrice)
		self.possibilities_first = self.possibilities
		self.possibilities = []

		for i, matrice in enumerate(self.possibilities_first):
			self.place_piece_on_piece_all_rotate(self.next, matrice)
			self.possibilities_second.append((self.possibilities, i))
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
		Hauteur = len(matrice)
		for row in range(Hauteur - 1, -1, -1):
			cpMatrice = my_copy(matrice)
			if self.replace_in_matrice(x, row, piece, cpMatrice):
				self.tmpPossible.append(cpMatrice)
				break
			
	def replace_in_matrice(self, x, y, piece, matrice):
		Largeur = len(piece[0])
		Hauteur = len(piece)
		if len(matrice[0]) - x < Largeur:
			return 0
		try:
			# if self.check_can_place_under_shadow(x, y + Hauteur - 1, Hauteur, Largeur, piece, matrice) == 0:
			#     return 0
			if self.check_playable(x, y, Hauteur, Largeur, piece, matrice) == False:
				return 0
			# y = self.check_downable(x, y, Hauteur, Largeur, piece, matrice)
			for yPiece in range(Hauteur)[::-1]:
				for xPiece in range(Largeur):
						if piece[yPiece][xPiece] == 2:
							self.place_one_pixel(x + xPiece, y + yPiece, matrice)
		except :
			return 0
		return 1

	def check_playable(self, x, y, PHauteur, PLargeur, piece, matrice):
		for i in range(PHauteur)[::-1]:
			for j in range(PLargeur):
				if piece[i][j] == 2 and matrice[y + i][x + j] != 0: #Modify to include shadows
					return False
		return True

	# def check_downable(self, x, y, PHauteur, PLargeur, piece, matrice):
	#     i = y + 1
	#     hauteur = len(matrice)
	#     while i < hauteur:
	#         for j in range(PLargeur):
	#             if matrice[i][x + j] == 2:
	#                 return i - PHauteur
	#         i += 1
	#     return i - PHauteur

	# def check_can_place_under_shadow(self, x, y, PHauteur, PLargeur, piece, matrice):
	#     i = 0
	#     overShadow = 0
	#     largeur = len(matrice[0])
	#     while i < largeur:
	#         if (matrice[y][x + i] == 0):
	#             overShadow += 1
	#         elif matrice[y][x + i] == 1:
	#             overShadow = 0
	#         elif matrice[y][x + i] == 2:
	#             overShadow = 0
	#         if overShadow >= PLargeur:
	#             return 1
	#         i += 1
	#     return 0

	def place_one_pixel(self, x, y, matrice):
		Hauteur = len(matrice)
		matrice[y][x] = 2
		for i in range(y + 1, Hauteur):
			if matrice[i][x] == 0:
				matrice[i][x] = 1
	
	def rotate_piece(self, piece):
		piece_pivotee = [[piece[j][i] for j in range(len(piece))] for i in range(len(piece[0])-1, -1, -1)]
		return piece_pivotee

	def send_best_map(self):
		best_map = (None, None, None)
		for possibility in self.possibilities_second:
			index = possibility[1]
			for matrice in possibility[0]:
				score = return_scoring(matrice)
				if best_map == (None, None, None):
					best_map = (score, self.possibilities_first[index])
				elif score < best_map[0]:
					best_map = (score, self.possibilities_first[index])
		return (best_map[1])

def check_execution_time():
	start = time.time()
	matrice = [[0  for _ in range(12)] for _ in range(22)]
	algorithm = Algo('J', 'S', matrice)
	algorithm.place_piece_and_create_list()
	bestMap = algorithm.send_best_map()
	matrice = clear(bestMap)
	algorithm = Algo('S', 'T', matrice)
	algorithm.place_piece_and_create_list()
	bestMap = algorithm.send_best_map()
	matrice = clear(bestMap)
	algorithm = Algo('T', 'O', matrice)
	algorithm.place_piece_and_create_list()
	bestMap = algorithm.send_best_map()
	matrice = clear(bestMap)
	algorithm = Algo('O', 'I', matrice)
	algorithm.place_piece_and_create_list()
	bestMap = algorithm.send_best_map()
	print("EXECUTION TIME : ", time.time() - start)

if __name__ == '__main__':
	check_execution_time()
