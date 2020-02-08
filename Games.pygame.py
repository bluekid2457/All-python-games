import pygame
from tron import Tron
from Pong import pong
from tictactoe import tic
from snake import snake

pygame.init()
mainscreen = pygame.display.set_mode((600,500))
troncover = pygame.image.load('Troncover.jpeg')
pongcover = pygame.image.load('pong.png')
ticcover = pygame.image.load('ticsymbol.png')
snakecover = pygame.image.load('snake.jpeg')

pos=(-5,-5)
allrunning = True
while allrunning == True:
    pygame.time.delay(100)
    mainscreen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            allrunning = False


    if event.type == pygame.MOUSEBUTTONDOWN:
      pos = pygame.mouse.get_pos()
      
      if (pos[0] > 0) and pos[1] > 0 and (pos[0]) <= 132 and (pos[1]) < 300:
          Tron()
          pygame.mouse.set_pos(-10,-10)
      if (pos[0]) > 132 and (pos[0]) <= 432 and (pos[1]) < 300:
          pong()
          pygame.mouse.set_pos(-10,-10)
      if (pos[0]) > 0 and pos[0] < 200 and pos[1] > 301 and pos[1] < 500:
          tic()
          pygame.mouse.set_pos(-10,-10)
      if (pos[0]) > 200 and (pos[0]) <= 500 and (pos[1]) > 301:
          snake()
          pygame.mouse.set_pos(-10,-10)
          

    print(pos)
    
    pos = (-5,-5)
    
      
    mainscreen.blit(troncover,(0,0))
    mainscreen.blit(pongcover,(133,0))
    mainscreen.blit(ticcover,(0,300))
    mainscreen.blit(snakecover,(201,300))
    pygame.display.update()
    

pygame.quit()

