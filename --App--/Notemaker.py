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
from pygame import font
from pygame import draw
import time
from os import path
from os import getcwd
from os import listdir
from os import startfile
from subprocess import call

curr_dir = getcwd()
curr_dir = curr_dir[:-8]

class Notemaker():
    def __init__(self, gameWindow):
        init()

        self.gw = gameWindow

    def main(self):
        self.game_setup()

        running = True
        while running:
            for ev in event.get():
                if ev.type == quit():
                    running = False

    def game_setup(self):
        self.gw = display.set_mode((275, 385))
        display.set_caption('Notemaker')
        bga = path.join(curr_dir, "Requirements\g_notemaker bg_a.png")
        bgb = path.join(curr_dir, "Requirements\g_notemaker bg_b.png")
        icon = image.load(path.join(curr_dir, "Requirements\icon.png"))
        bg_a = image.load(bga)
        bg_b = image.load(bgb)
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
                    if area_a.collidepoint(ev.pos) :
                        new_note = path.join(curr_dir, 'Modules\\new_note.py')
                        call(new_note, shell = True)
                    if area_b.collidepoint(ev.pos) :
                        notes = path.join(curr_dir, 'Modules\\notes.py')
                        #exec(open(notes).read())
                        call(notes, shell = True)
                                                       
                num = ev.type
                if num == 256 :
                    running = False
            
        quit() 
        
game = Notemaker(None)
game.main()