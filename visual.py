import cv2 as cv
from enum import Enum
import pyautogui as gui
#from pynput.keyboard import Key, Listener
import time as t
import utils

class Game:

    H_SIZE = 12
    V_SIZE = 22
    WHITE_COLUMN = 37
    BROWN_COLUM = 33
    SQUARE = 33
	
    def __init__(self):
        self.actual_piece = 'E'
        self.next_piece = 'E'
        self.state = 1
        self.board_coord = None
        self.matrice = [[0  for _ in range(Game.H_SIZE)] for _ in range(Game.V_SIZE)]
        self.get_visual_data()

    def Color_piece(self, Color):
        match Color:
            case (234, 51, 35):
                return 'I'
            case (190, 91, 191):
                return 'T'
            case (86, 162, 243):
                return 'J'
            case (243, 176, 68) :
                return 'S'
            case (153, 153, 153):
                return 'O'
            case (101, 193, 94):
                return 'L'
            case (237, 112, 45):
                return 'Z'
            case _:
                return 'E'

    def get_actual_piece(self):
            block1 = self.Color_piece(gui.pixel(1106, 191))
            block2 = self.Color_piece(gui.pixel(1102, 229))
            if (block1 != 'E'):
                print("Current Block found : " + block1)
                self.actual_piece = block1
            if (block2 != 'E' and block1 == 'E'):
                print("Current Block found : " + block2)
                self.actual_piece = block2

    def get_next_piece(self):
            block1 = self.Color_piece(gui.pixel(713, 545))
            block2 = self.Color_piece(gui.pixel(715, 578))
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
            except:
                print("Fail during board recognition, trying again in 3 seconds...")
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
        for j in range(Game.V_SIZE, y, -1):
            screen_y -= Game.SQUARE
        #Offset to center of the piece
        screen_x += Game.SQUARE / 2
        screen_y -= Game.SQUARE / 2
        #DEV
        #gui.moveTo(screen_x, screen_y)
        return (self.Color_piece(gui.pixel(int(screen_x), int(screen_y))))

    def insert_piece(self, x, y, direction):
        while (self.get_cell(x, y) == 'E'):
            t.sleep(0.01) #NEED TESTING
        old_piece = self.actual_piece
        while (self.actual_piece == old_piece):
            gui.press(direction)
            t.sleep(0.01) #NEED TESTING
            self.get_actual_piece()

    def get_visual_data(self):
        self.get_board_coord()
        gui.click(self.board_coord.left + 160, self.board_coord.top + 90)
        start = t.time()
        while (self.actual_piece == 'E' and self.next_piece == 'E' and t.time() - start < 3):
            self.get_actual_piece()
            self.get_next_piece()
        if (t.time() - start >= 3):
            print("TIMEOUT PIECES NOT FOUND")

    def update_pieces(self):
        start = t.time()
        old_piece = self.actual_piece
        while (old_piece == self.actual_piece and t.time() - start < 3):
            self.get_actual_piece()
            self.get_next_piece()
        if (t.time() - start >= 3):
            print("TIMEOUT PIECES NOT FOUND")
