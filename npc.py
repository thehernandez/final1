import pygame 
import random 
import math 
LEFT = 9 
RIGHT = 1 
UP = 2 
DOWN = 3 

class npc: 
    def __init__(self): 
        self.xpos = 100
        self.ypos = 500 
        self.direction = RIGHT 
        self.isAlive = True 

    def draw(self,sceen): 
        if self.isAlive == True: 
            pygame.draw.circle(screen, (0,0,250), (self.xpos, self.ypos), 20)