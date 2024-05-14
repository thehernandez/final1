import pygame
import math
from player import player
from fireball import fireball
from enemy import enemy
pygame.init()
pygame.display.set_caption("top down grid game")# window tile
screen = pygame.display.set_mode((1200,900))#game screen
clock = pygame.time.Clock()#set up clock
gameover = False#variable game loop

#instantiatre player
p1 = player()
ball = fireball()
michael = enemy()
ticker = 0 
#constants
LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3
SPACE = 4
ENTER = 5
keys = [False, False, False, False, False, False] # this list hgoldd whether each key has been pressed 
mapNum = 1

map = [[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
       [2,1,1,1,1,2,2,1,1,0,0,1,1,1,1,2,2,1,1,2,2,2,2,2],
       [2,1,1,1,1,2,2,1,1,0,0,1,1,1,1,2,2,1,1,3,3,3,3,2],
       [2,0,0,2,2,2,2,0,0,0,0,0,0,2,2,2,2,0,0,3,3,3,3,2],
       [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,3,3,3,2],
       [2,0,0,0,0,0,2,2,0,0,0,0,0,0,0,0,2,2,0,3,3,3,3,2],
       [2,3,2,3,3,3,2,2,0,0,0,3,2,3,3,3,2,2,0,3,3,3,3,2],
       [2,3,3,3,3,3,0,0,0,0,0,3,2,3,3,3,0,0,0,3,3,3,3,2],
       [5,3,3,3,3,0,0,0,0,0,0,3,2,3,3,0,0,0,0,3,3,3,3,5],
       [5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5],
       [2,1,1,1,1,2,2,1,1,0,0,1,1,1,1,2,2,1,1,3,3,3,3,2],
       [2,1,1,1,1,2,2,1,1,0,0,1,1,1,1,2,2,1,1,3,3,3,3,2],
       [2,0,0,2,2,2,2,0,0,0,0,0,0,2,2,2,2,0,0,3,3,3,3,2],
       [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,3,3,3,2],
       [2,0,0,0,0,0,2,2,0,0,0,0,0,0,0,0,2,2,0,3,3,3,3,2],
       [2,3,2,3,3,3,2,2,0,0,0,3,2,3,3,3,2,2,0,3,3,3,3,2],
       [2,3,2,3,3,3,0,0,0,0,0,3,2,3,3,3,0,0,0,3,3,3,3,2],
       [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]]

map2 = [[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
       [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
       [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
       [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
       [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
       [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
       [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
       [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
       [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,5],
       [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,5],
       [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
       [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
       [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
       [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
       [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
       [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
       [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
       [3,3,3,3,3,3,3,3,3,3,3,5,5,3,3,3,3,3,3,3,3,3,3,3]]

brick = pygame.image.load('brick.png')
dirt = pygame.image.load('dirt.png')
grass = pygame.image.load('grass.png')


def draw(drawPlayer):
    screen.fill((0,0,0))#wipe screen
    
        
        #print(p1.vx, p1.vy, p1.xpos, p1.ypos)
    if mapNum == 1:    #map
        for i in range(len(map)):
            for j in range(len(map[i])):
                if map[i][j] == 1:
                    screen.blit(dirt, (j * 50, i * 50), (0, 0, 50, 50))
                if map[i][j] == 2:
                    screen.blit(brick, (j * 50, i * 50), (0, 0, 50, 50))
                if map[i][j] == 3:
                    screen.blit(grass, (j * 50, i * 50), (0, 0, 50, 50))
    elif mapNum == 2:    #map
        for i in range(len(map)):
            for j in range(len(map[i])):
                if map2[i][j] == 1:
                    screen.blit(dirt, (j * 50, i * 50), (0, 0, 50, 50))
                if map2[i][j] == 2:
                    screen.blit(brick, (j * 50, i * 50), (0, 0, 50, 50))
                if map2[i][j] == 3:
                    screen.blit(grass, (j * 50, i * 50), (0, 0, 50, 50))


    if drawPlayer == True:
        p1.draw(screen)
    if ball.isAlive == True:
            ball.draw(screen)
        
    michael.draw(screen)

    pygame.draw.rect(screen, (255, 255, 255), (750, 5, 200, 30))
    pygame.draw.rect(screen, (150, 0, 0), (750, 5, p1.health, 30))
    pygame.draw.rect(screen, (0, 0, 0), (750, 5, 200, 30), 3)                
    pygame.display.flip()
def dist(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2**2)**2)



while not gameover:
    clock.tick(60)#fps
    ticker += 1
    #input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:#quit game if x is presed in top corner
            gameover = True
        if event.type == pygame.KEYDOWN:#quit game if x is presed in top corner
            if event.key == pygame.K_LEFT:
                keys[LEFT] = True
            
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT] = True
            elif event.key == pygame.K_UP:
                keys[UP] = True
            elif event.key == pygame.K_DOWN:
                keys[DOWN] = True
            
            if event.key == pygame.K_SPACE:
                keys[SPACE] = True
        
        
        elif  event.type == pygame.KEYUP:#quit game if x is presed in top corner
            if event.key == pygame.K_LEFT:
                keys[LEFT] = False
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT] = False
            elif event.key == pygame.K_UP:
                keys[UP] = False
            elif event.key == pygame.K_DOWN:
                keys[DOWN] = False
            
            if event.key == pygame.K_SPACE:
                keys[SPACE] = False
        
    #pycals
    if keys[SPACE] == True:
        ball.shoot(p1.xpos, p1.ypos, p1.direction)
    
    if mapNum == 1:
        michael.move(map, ticker, p1.xpos, p1.ypos)
        michael.draw(screen)
        michael.die(ball.xpos, ball.ypos)

        #p1.die(michael.xpos, michael.ypos)
        #p1.ouch(michael.xpos, michael.ypos)
        p1.move(keys, map)
        ball.move()
        if keys[ENTER] == True and dist(p1.xpos, p1.ypos)<10:
            n1.talk()
    elif mapNum == 2:
        michael.move(map2, ticker, p1.xpos, p1.ypos)
        michael.draw(screen)
        michael.die(ball.xpos, ball.ypos)
        p1.move(keys, map)
        ball.move()

    
    
    
    if mapNum == 1:
        if map[int((p1.ypos ) / 50)][int( (p1.xpos) / 50)] == 5:
            mapNum =2
            p1.xpos = 1100
    if mapNum == 2:
        if map[int((p1.ypos ) / 50)][int( (p1.xpos) / 50)] == 5:
            mapNum =1
            p1.xpos = 100
    if mapNum == 3:
        if map[int((p1.ypos ) / 50)][int( (p1.xpos) / 50)] == 5:
            mapNum =1
            p1.xpos = 50

    #render
    draw(True)

pygame.quit()