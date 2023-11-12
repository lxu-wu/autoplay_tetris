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
		# print(Tetris.actual_piece, Tetris.next_piece)
		algorithm = Algo(Tetris.actual_piece, Tetris.next_piece, copy.deepcopy(matrice))
		algorithm.place_piece_and_create_list()
		bestMap = algorithm.send_best_map()
		# for m in algorithm.matrice:
		# 	print(m,end="\n")
		# print("\n")
		# for m in bestMap:
		# 	print(m,end="\n")
		# print()
	
    
		

		tuple = algorithm.deplacement_pieces(copy.deepcopy(matrice), copy.deepcopy(bestMap), algorithm.curr) #action, position
		for action in tuple[0]:
			gui.press(action)
		# t.sleep(0.3)
		algorithm = None
		matrice = clear(bestMap)
		Tetris.update_pieces()
