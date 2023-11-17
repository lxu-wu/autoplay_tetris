#from visual import Game

import numpy as np
import copy
import unittest
# Define Tetris pieces

def is_full(line):
	return all(val == 2 for val in line)

def clear_shadow(matrix):
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			if (matrix[i][j] == 1 and i > 0 and matrix[i - 1][j] == 0):
				matrix[i][j] = 0

def clear(board):
	y = len(board)
	x = len(board[0])
	cleared_board = []
	for index, line in enumerate(board):
		if not is_full(line):
			cleared_board.append(line)
	while len(cleared_board) < y:
		cleared_board.insert(0, [0 for _ in range(x)])
	#retirer les ombres qui ne sont plus des ombres
	clear_shadow(cleared_board)
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

def change_ones_to_zeros(matrice):
	new_matrice = my_copy(matrice)
	for i in range(len(new_matrice)):
		for j in range(len(new_matrice[i])):
			if new_matrice[i][j] == 1:
				new_matrice[i][j] = 0
	return new_matrice

def only_zeros_and_twos(matrice):
	for i in range(len(matrice)):
		for j in range(len(matrice[0])):
			if matrice[i][j] != 0 and matrice[i][j] != 2 and matrice[i][j] != 1:
				return False
	return True

def my_copy(mat):
    return [row[:] for row in mat]

class clear_test(unittest.TestCase):

	def test_empty_matrix(self):
		matrice = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
		self.assertEqual(matrice, clear(matrice))

	def test_clear_above(self):
		matrice = [[2, 2, 2], [2, 1, 2], [2, 2, 2]]
		final_matrice = [[0, 0, 0], [0, 0, 0], [2, 0, 2]]
		self.assertEqual(clear(matrice), final_matrice)

	def test_shadow_clear(self):
		matrice = [[2, 2, 2], [1, 1, 1], [1, 1, 1]]
		final_matrice = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
		self.assertEqual(clear(matrice), final_matrice)

	def test_clear_below(self):
		matrice = [[0, 0, 0], [2, 0, 2], [2, 2, 2]]
		final_matrice = [[0, 0, 0], [0, 0, 0], [2, 0, 2]]
		self.assertEqual(clear(matrice), final_matrice)

class my_copy_test(unittest.TestCase):
	def test_copy(self):
		matrice1 = [[1, 2]]
		matrice2 = my_copy(matrice1)
		self.assertEqual(matrice1, matrice2)
	def test_change(self):
		matrice1 = [[1, 2]]
		matrice2 = my_copy(matrice1)
		matrice2[0][0] = 0
		self.assertNotEqual(matrice1, matrice2)
	def test_change_completely(self):
		matrice1 = [[1, 2]]
		matrice2 = my_copy(matrice1)
		matrice2 = [[0, 0]]
		self.assertNotEqual(matrice1, matrice2)


if __name__ == '__main__':
	unittest.main()
	my_copy_test()