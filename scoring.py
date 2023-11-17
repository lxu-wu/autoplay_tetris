import copy
from utils import *
import unittest
import time

HEIGHT_MUL = 2
SHADE_MUL = 5 #Need to change when he can insert
HOLE_MUL = 5
CLEARED_LINES_MUL = 5

class Score:
	
	def __init__(self):
		self.sum_height = 0
		self.hole = 0
		self.shade = 0
		self.cleared_lines = 0

	def get_scoring_data(self, matrice):
		after_matrice = clear(matrice)
		for i, row in enumerate(after_matrice):
			if is_full(matrice[i]):
				self.cleared_lines += 1
			for j, cell in enumerate(row):
				if (cell == 1):
					self.shade +=1
					if (self.is_hole(after_matrice, i, j)):
						self.hole +=1
				if (cell == 2):
					self.sum_height += (len(after_matrice) - i)


	def is_hole(self, matrice, i, j):
		is_trapped = True
		#is trapped on the left ?
		for j2 in range(j, -1, -1):
			if (matrice[i][j2] == 2 or not is_trapped):
				break
			if (matrice[i][j2] == 0):
				is_trapped = False
		#is trapped on the right ?
		for j2 in range(j, len(matrice[i])):
			if (matrice[i][j2] == 2 or not is_trapped):
				break
			if (matrice[i][j2] == 0):
				is_trapped = False
		#is trapped up ?
		for i2 in range(i, -1, -1):
			if (matrice[i2][j] == 2 or not is_trapped):
				break
			if (matrice[i2][j] == 0):
				is_trapped = False
		#is trapped down ?
		for i2 in range(i, len(matrice)):
			if (matrice[i2][j] == 2 or not is_trapped):
				break
			if (matrice[i2][j] == 0):
				is_trapped = False
		return (is_trapped)

def return_scoring(matrice):
	data = Score()
	data.get_scoring_data(matrice)
	score = (data.sum_height * HEIGHT_MUL) + (data.hole * HOLE_MUL) + (data.shade - data.hole) * SHADE_MUL
	score -= data.cleared_lines * CLEARED_LINES_MUL
	return score	

class TestIsHole(unittest.TestCase):

	def test_empty_space(self):
		matrice = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
		self.assertFalse(Score.is_hole(self, matrice, 1, 1))

	def test_wall(self):
		matrice = [[2, 2, 2], [2, 1, 2], [2, 2, 2]]
		self.assertTrue(Score.is_hole(self, matrice, 1, 1))

	def test_space_with_wall_above(self):
		matrice = [[2, 2, 2], [2, 1, 2], [1, 1, 1]]
		self.assertTrue(Score.is_hole(self, matrice, 1, 1))

	def test_space_with_wall_below(self):
		matrice = [[0, 0, 0], [2, 1, 2], [2, 2, 2]]
		self.assertFalse(Score.is_hole(self, matrice, 1, 1))

if __name__ == '__main__':
	unittest.main()
