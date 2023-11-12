from algo import *
from visual import Game
from utils import *
import pyautogui as gui
import time as t

def go_to_position(position):
     gui.press('right', position[0])

if (__name__ == "__main__"):
	Tetris = Game()
	while (1):
		algorithm = Algo(Tetris.actual_piece, Tetris.next_piece, Tetris.matrice)
		algorithm.place_piece_and_create_list()
		bestMap = algorithm.send_best_map()
		if (bestMap != None):
			tuple = algorithm.rotations(algorithm.matrice, bestMap, Tetris.actual_piece) #action, position
		else:
			print("no map")
		for action in tuple[0]:
			gui.press(action)
		go_to_position(tuple[1])
		gui.press('space')
		t.sleep(0.3)
		algorithm.matrice = bestMap
		Tetris.matrice = algorithm.matrice
		Tetris.update_pieces()
