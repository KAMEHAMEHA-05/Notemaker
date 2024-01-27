# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 19:00:49 2021

@author: Admin
"""

from pygame import image
from pygame import init
from pygame import display
from pygame import Rect
from pygame import event
from pygame import quit
from pygame import MOUSEBUTTONDOWN
import time
import os

class Notemaker():
    def __init__(self, gameWindow):
        init()

        self.gw = gameWindow

    def main(self):
        self.game_setup()

        running = True
        while running:
            for ev in event.get():
                if ev.type == QUIT:
                    running = False

    def game_setup(self):
        self.gw = display.set_mode((275, 385))
        display.set_caption('Notemaker')
        icon = image.load(r"G:\SACS\Computer Science\Projects\Notemaker\Requirements\Screenshot (942).png")
        bg_a = image.load(r"G:\SACS\Computer Science\Projects\Notemaker\Requirements\notemaker bg_a.png")
        bg_b = image.load(r"G:\SACS\Computer Science\Projects\Notemaker\Requirements\notemaker bg_b.png")
        area_a = Rect(37, 109, 200, 107)
        area_b = Rect(37, 238, 200, 107)
        display.set_icon(icon)
        self.gw.blit(bg_a, (0,0))
        display.flip()
        time.sleep(2)
        self.gw.blit(bg_b, (0,0))
#        pygame.draw.rect(self.gw, (100, 20, 10), area_b)
        display.flip()
        
        running = True
        while running : 
            for ev in event.get():
                if ev.type == MOUSEBUTTONDOWN:
                    if area_a.collidepoint(event.pos) :
                        print('Area 1 clicked.')
                    if area_b.collidepoint(event.pos) :
                        print('Area 2 clicked.')
                                                       
                num = ev.type
                if num == 256 :
                    print("Quit")
                    running = False
            
        quit() 
        
game = Notemaker(None)
game.main()