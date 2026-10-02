import pygame
from vector2 import *


class Button():

    def __init__(self, name, pos, size, func, ScreenSize):

        self.ScreenSize = ScreenSize
        self.name = name
        self.pos = pos
        self.size = size
        self.func = func
        self.MouseOver = False

    
    def Update(self, events):

        MousePos = Vector2.PygameVectorToVector2(pygame.mouse.get_pos())

        if self.pos.x < MousePos.x and MousePos.x < (self.pos.x + self.size.x):

            if self.ScreenSize[1] - self.pos.y > MousePos.y and MousePos.y > self.ScreenSize[1] - (self.pos.y + self.size.y):

                self.MouseOver = True

            else:

                self.MouseOver = False
        
        else:

            self.MouseOver = False

        for event in events:

            if self.MouseOver == True and event.type == pygame.MOUSEBUTTONUP:

                self.func("hola")




        


'''class Menu:

    def __init__(self):

        self.ButtonArray = []


    def AddButton(self, button):'''
