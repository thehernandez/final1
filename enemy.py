import pygame 
import random 
import math

LEFT = 0
RIGHT = 1 
UP = 2
DOWN = 3

class enemy: 
    def __init__ (self):
        self.xpos = 100 
        self.ypos = 500
        self.direction = RIGHT 
        self.isAlive = True 
        
    def draw(self,screen): 
        pygame.draw.rect(screen, (233,50,73), (self.xpos, self.ypos, 30, 30))

    def move(self, map, ticker, px, py):
    #randomly wander: 
        if ticker % 40 == 0: 
            num = random.randrange(0,4) 
            if num == 0:
                self.direction = RIGHT 
            elif num == 1: 
                self.direction = LEFT
            elif num == 2:
                self.direction = UP 
            elif num == 3:
                self.direction = DOWN 
        #check were player is enemy 
        if abs(int(py/50) - int(self.ypos/50))<2:
            if px < self.xpos:
                self.xpos-=1
                self.direction = LEFT
            else:
                self.xpos+=1
                self.direction = RIGHT
        if abs(int(px/50) - int(self.xpos/50))<2:
            if py < self.ypos:
                self.ypos-=1
                self.direction = LEFT
            else:
                self.ypos+=1
                self.direction = RIGHT


                #check for wall collision and change diraction if bumped 
        #print("checking", int((self.ypos ) / 50), int( (self.xpos + 20) / 50))
        if self.direction == RIGHT and map[int((self.ypos ) / 50)][int( (self.xpos + 20) / 50)] == 2: #this line croaks!
            self.direction = UP 
            self.xpos -= 6 

        if self.direction == LEFT and map[int((self.ypos ) / 50 )][int((self.xpos - 20) / 50)] == 2: 
            self.direction = DOWN 
            self.xpos += 6
                
        if self.direction == RIGHT: 
            self.xpos += 3 
        elif self.direction == LEFT: 
            self.xpos -= 3 
            
    def die(self, ballx, bally): 
            if math.sqrt((self.xpos-ballx)**2 + (self.ypos-bally)**2) <= 20: 
                    self.isAlive = False