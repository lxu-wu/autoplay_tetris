from algo import *
from visual import Game
from utils import *
import pyautogui as gui

if (__name__ == "__main__"):
	Tetris = Game()
	while (1):
		algorithm = Algo(Tetris.actual_piece, Tetris.next_piece, Tetris.matrice)
		algorithm.place_piece_and_create_list()
		bestMap = algorithm.send_best_map()
		tuple = algorithm.rotations(algorithm.matrice, bestMap) #action, position
		for action in tuple[0]:
			gui.press(action)
		Tetris.update_pieces()


