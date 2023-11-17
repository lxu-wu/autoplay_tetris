from algo import *
from visual import Game
from utils import *
import pyautogui as gui
import time as t
import copy
import cProfile
from movement import deplacement_pieces

def print_mat(matrix):
	for line in matrix:
		print(line)
	print("")

def play():
	Tetris = Game()
	matrice = [[0  for _ in range(12)] for _ in range(22)]
	while (Tetris.state):
		algorithm = Algo(Tetris.actual_piece, Tetris.next_piece, matrice)
		algorithm.place_piece_and_create_list()
		bestMap = algorithm.send_best_map()
		tuple = deplacement_pieces(matrice, bestMap, algorithm.curr)
		gui.press(tuple[0])
		gui.press('space')
		Tetris.update_pieces()
		matrice = clear(bestMap)

if __name__ == '__main__':
	play()
	# cProfile.run('play()')