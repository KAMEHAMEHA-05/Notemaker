# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 18:07:16 2021

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
from os import path
from os import getcwd
from os import listdir
from os import startfile

#curr_dir = getcwd()
#curr_dir = curr_dir[:-4]
#pth = path.join(curr_dir,"Notes")
#edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

class Notemaker():
    def __init__(self, gameWindow):
        init()

        self.g_w = gameWindow

    def main(self):
        self.game_setup()

        running = True
        while running:
            for ev in event.get():
                if ev.type == quit():
                    running = False

    def game_setup(self):
        curr_dir = getcwd()
        curr_dir = curr_dir[:-8]
        pth = path.join(curr_dir,"Notes")
        print(pth)
        edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
        self.g_w = display.set_mode((275, 385))
        req = "Requirements\g_notes_bg.png"
        n_bg_a = path.join(curr_dir,req)
        print(n_bg_a)
        notes_bg_a = image.load(n_bg_a)
        self.g_w.blit(notes_bg_a, (0,0))
        display.flip()
        h = 55
        counter = 1
        for path_ in listdir(pth):
            locals()[path_] = Rect(1, h, 272, 35)
            draw.rect(self.g_w, (0, 0, 0), locals()[path_], 1)
            font_ = font.Font(font.get_default_font(), 18)
            text_surface = font_.render(path_, True, (0, 0, 0))
            self.g_w.blit(text_surface, dest=(5,h+7))
            display.flip()
            h = h+36 
            counter = counter +1
            if counter == 9:
                h=h+3
                show_all = Rect(87, h, 100, 35)
                show_all_color = Rect(87, h, 100, 35)
                draw.rect(self.g_w, (124, 185, 232), show_all_color)
                draw.rect(self.g_w, (0, 0, 0), show_all, 1)
                font_ = font.Font(font.get_default_font(), 18)
                text_surface = font_.render("Show All", True, (0, 0, 0))
                self.g_w.blit(text_surface, dest=(96,h+7))
                display.flip()
                break
            
        running = True
        while running : 
            counter = 1
            for eve in event.get():
                if eve.type == (MOUSEBUTTONDOWN):
                    for path_ in listdir(pth):
                        if locals()[path_].collidepoint(eve.pos) :
                            note = path.join(pth, path_)
                            startfile(note)
                        counter = counter+1
                        if counter == 9 :
                            break
                    if counter == 9 and show_all.collidepoint(eve.pos) :
                        startfile(pth)
                        
                num = eve.type
                if num == 256 :
                    running = False
            
        quit() 
        
        
game = Notemaker(None)
game.main()