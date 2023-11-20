import cv2 as cv
from enum import Enum
import pyautogui as gui
#from pynput.keyboard import Key, Listener
import time as t
import utils
import copy

class Game:

	SCALING = 1 + 1.75
	H_SIZE = 12
	V_SIZE = 22
	WHITE_COLUMN = 15 * SCALING
	BROWN_COLUM = 13 * SCALING
	SQUARE = 13 * SCALING

	def __init__(self):
		self.actual_piece = 'E'
		self.next_piece = 'E'
		self.state = 1
		self.board_coord = None
		self.matrice = [[0  for _ in range(Game.H_SIZE)] for _ in range(Game.V_SIZE)]
		self.get_visual_data()
		gui.PAUSE = 0.05

	def Color_piece(self, Color):
		match Color:
			case (255, 0, 0):
				return 'I'
			case (204, 84, 196):
				return 'T'
			case (50, 164, 250):
				return 'J'
			case (255, 172, 28) :
				return 'S'
			case (153, 153, 153):
				return 'O'
			case (56, 196, 79):
				return 'L'
			case (255, 102, 0):
				return 'Z'
			case _:
				return 'E'

	def get_actual_piece(self):
			x = 1106
			y = 191 + 33
			y2 = y + 33
			block1 = self.Color_piece(gui.pixel(x, y))
			block2 = self.Color_piece(gui.pixel(x, y2))
			if (block1 != 'E'):
				print("Current Block found : " + block1)
				self.actual_piece = block1
				return (1)
			if (block2 != 'E' and block1 == 'E'):
				print("Current Block found : " + block2)
				self.actual_piece = block2
				return (1)
			return (0)

	def get_next_piece(self):
			x = int(self.board_coord.left + 51 * Game.SCALING)
			y = int(self.board_coord.top + 159 * Game.SCALING)
			y2 = int(y - Game.SQUARE)
			block1 = self.Color_piece(gui.pixel(x, y))
			block2 = self.Color_piece(gui.pixel(x, y2))
			if (block1 != 'E'):
				print("Next Block found : " + block1)
				self.next_piece = block1
			if (block2 != 'E' and block1 == 'E'):
				print("Next Block found : " + block2)
				self.next_piece = block2
		
	def get_board_coord(self):
		while(1):
			try:
				self.board_coord = gui.locateOnScreen('game.png', grayscale=True, confidence=0.9)
				print("Success : Board found")
				break
			except Exception as e:
				print(e, "Fail during board recognition, trying again in 3 seconds...")
				t.sleep(3)

	def get_cell(self, x, y):
		#get down right corner
		screen_x = self.board_coord.left + self.board_coord.width
		screen_y = self.board_coord.top + self.board_coord.height
		#Offset to wanted piece
		for i in range(Game.H_SIZE, x, -1):
			if (i % 2 == 0):
				screen_x -= Game.WHITE_COLUMN
			else:
				screen_x -= Game.BROWN_COLUM
		for j in range(Game.V_SIZE, y + 1, -1):
			screen_y -= Game.SQUARE
		#Offset to center of the piece
		screen_x += Game.SQUARE
		screen_y -= Game.SQUARE
		#DEV
		gui.moveTo(screen_x, screen_y)
		return (self.Color_piece(gui.pixel(round(screen_x), round(screen_y))))

	def insert_piece(self, x, y, direction):
		start = t.time()
		while (self.get_cell(x, y) == 'E' and t.time() - start < 25):
			t.sleep(0.01)
		if (t.time() - start >= 25):
			print("TIMEOUT Insertion")
		old_piece = self.actual_piece
		while (self.actual_piece == old_piece):
			gui.press(direction)
			self.get_actual_piece()

	def get_visual_data(self):
		self.get_board_coord()
		x = int(59 * Game.SCALING)
		y = int(44 * Game.SCALING)
		gui.click(self.board_coord.left + x, self.board_coord.top + y)
		self.update_pieces()
			# print("TIMEOUT PIECES NOT FOUND")

	def look_for_end_game(self):
		try:
			gui.locateOnScreen('end_game.png', grayscale=True, confidence=0.5)
			gui.write("TheAmazingBOT")
			gui.press("enter")
			self.state = 0
		except:
			pass

	def update_pieces(self):
		while (self.get_actual_piece() == 0):
			t.sleep(0.05)
		self.get_next_piece()
		#self.look_for_end_game()

if __name__ == '__main__':
	Test = Game()
	Test.get_actual_piece()