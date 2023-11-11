import cv2 as cv
from enum import Enum
import pyautogui as gui
from pynput import keyboard
import time as t

class Game:

    def __init__(self):
        self.board = Board()
        self.actual_piece = 'E'
        self.next_piece = 'E'
        self.state = 1
    
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
            screenshot = gui.screenshot(region=(1100, 190, 1107, 230))
            block1 = self.Color_piece(screenshot.getpixel((1106 - 1100, 191 - 190)))
            block2 = self.Color_piece(screenshot.getpixel((1102 - 1100, 229 - 190)))
            if (block1 != 'E'):
                print("Current Block found : " + block1)
                self.actual_piece = block1
            if (block2 != 'E' and block1 == 'E'):
                print("Current Block found : " + block2)
                self.actual_piece = block2

    def get_next_piece(self):
            screenshot = gui.screenshot(region=(712, 544, 716, 579))
            block1 = self.Color_piece(screenshot.getpixel((713 - 712, 545 - 544)))
            block2 = self.Color_piece(screenshot.getpixel((715 - 712, 578 - 544)))
            if (block1 != 'E'):
                print("Next Block found : " + block1)
                self.s_piece = block1
            if (block2 != 'E' and block1 == 'E'):
                print("Next Block found : " + block2)
                self.s_piece = block2

class Board:
    #Block vide -> 0
    #Block vide mais toit -> 1
    #Block rempli -> 2

    def __init__(self):
        self.board = self.createBoard()

    def createBoard(self):
        mat = []
        for i in range(21):
            row = []
            for j in range(12):
                row.append(0)
            mat.append(row)
        return mat
