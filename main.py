from algo import *
from visual import Game
from utils import *
import pyautogui as gui
import time as t
import copy

if (__name__ == "__main__"):
	Tetris = Game()
	matrice = [[0  for _ in range(12)] for _ in range(22)]
	while (1):
		print(Tetris.actual_piece, Tetris.next_piece)
		algorithm = Algo(Tetris.actual_piece, Tetris.next_piece, matrice)
		algorithm.place_piece_and_create_list()
		bestMap = copy.deepcopy(algorithm.send_best_map())
		for m in algorithm.matrice:

			print(m,end="\n")
		print("\n")
		for m in bestMap:
			print(m,end="\n")

		""""if (bestMap != None):
			tuple = algorithm.rotations(copy.deepcopy(algorithm.matrice), copy.deepcopy(bestMap), algorithm.curr) #action, position
		else:
			print("no map")
		for action in tuple[0]:
			gui.press(action)
		if (tuple[2] != None):
			Game.insert_piece(tuple[1])
		t.sleep(0.3)"""
		algorithm = None
		matrice = bestMap
		Tetris.update_pieces()
