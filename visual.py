import cv2 as cv
from enum import Enum
import pyautogui as gui
from pynput.keyboard import Key, Listener
import time as t
import utils

class Game:

    H_SIZE = 12
    V_SIZE = 22
    WHITE_COLUMN = 37
    BROWN_COLUM = 33
    SQUARE = 33

    def __init__(self):
        self.board = Board()
        self.actual_piece = 'E'
        self.next_piece = 'E'
        self.state = 1
        self.board_coord = self.get_board_coord()
    
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
                self.s_piece = block1
            if (block2 != 'E' and block1 == 'E'):
                print("Next Block found : " + block2)
                self.s_piece = block2
        
    def get_board_coord(self):
        while(1):
            try:
                Coord = gui.locateOnScreen('game.png', grayscale=True, confidence=0.9)
                print("Success : Board found")
                return (Coord)
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



class Board:
    #Block vide -> 0
    #Block vide mais toit -> 1
    #Block rempli -> 2

    def __init__(self):
        self.board = self.createBoard()

    def createBoard(self):
        mat = []
        for i in range(Game.V_SIZE):
            row = []
            for j in range(Game.H_SIZE):
                row.append(0)
            mat.append(row)
        return mat