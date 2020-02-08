def Tron():
  global facing
  import pygame
  import numpy
  import collections as cls


  pygame.init()

  screen = pygame.display.set_mode((600,500))
   
  start_ticks=pygame.time.get_ticks()
  start_ticks2=pygame.time.get_ticks()
  facing = 'right'
  length = 10
  p1bike_up = pygame.image.load('p1_up.jpeg')
  p1bike_down =pygame.image.load('p1_down.jpeg')
  p1bike_left =pygame.image.load('p1_left.jpeg')
  p1bike_right =pygame.image.load('p1_right.jpeg')
  class projectiles:
    def __init__(self, posx, posy, vel, size):
      self.posx = posx
      self.posy = posy
      self.vel = vel
      self.size = size
  def players(self):
      global facing
      
      keys=pygame.key.get_pressed()
      if keys[self.key_boost]:
        self.vel = 4
      else:
        self.vel = 2
      if keys[self.key_left] and self.facing!= 'right' and self.facing!='left':
        self.posx-=self.vel
        self.facing = 'left'
      elif keys[self.key_right] and self.facing!= 'left' and self.facing!='right':
        self.posx+=self.vel
        self.facing = 'right'
      elif keys[self.key_down] and self.facing!= 'down' and self.facing!='up':
        self.posy+=self.vel
        self.facing = 'down'
      elif keys[self.key_up] and self.facing!='up' and self.facing !='down':
        self.posy-=self.vel
        self.facing = 'up'

      elif self.facing == 'left':
        self.posx-=self.vel
        self.direction = p1bike_left

      elif self.facing == 'right':
        self.posx+=self.vel
        self.direction = p1bike_right
      
      elif self.facing == 'down':
        self.posy+=self.vel
        self.direction = p1bike_down

      elif self.facing == 'up':
        self.posy-=self.vel
        self.direction = p1bike_up

      if self.posx < 0:
        self.posx = 590
        print ('crashed')
        
      elif self.posy < 0:
        self.posy = 490
        print ('crashed')      
      elif self.posx > 590:
        self.posx = 0
        print ('crashed')
      elif self.posy > 490:
        self.posy = 0
        print ('crashed')
      
      k=-1
      
      try:
        while 1-k != len(self.xposes):
          pygame.draw.rect(screen,self.color,(self.xposes[k],self.yposes[k],5,5))
          k-=1
          length=1
      except:
        print('not')
      try: 
        #if len(self.xposes)>2:
          j = len(self.xposes)-2
          while j != 2 :
            if first.xposes[j]==(self.posx+(self.size/2)) and first.yposes[j] == (self.posy+(self.size/2)):
                print ('crashed')
                self.status = False
                
                #break
            if second.xposes[j]==(self.posx+(self.size/2)) and second.yposes[j] == (self.posy+(self.size/2)):
                print ('crashed')
                self.status = False
                #break
            j-=1
      except:
        print('just wait')
      self.xposes.append(self.posx+(first.size/2))
      self.yposes.append(self.posy+(first.size/2))
      screen.blit(self.direction, (self.posx+7,self.posy+7 ))
      #pygame.draw.rect(screen,self.color,(self.posx,self.posy,self.size,self.size))

  class blocks:
    def __init__(self, posx, posy, number, vel, size, xposes,yposes,key_left,key_right,key_up,key_down,key_boost,facing,color,status,direction):
      self.posx = posx
      self.posy = posy
      self.number = number
      self.vel = vel
      self.size = size
      self.xposes = xposes
      self.yposes = yposes
      self.key_left = key_left
      self.key_right = key_right
      self.key_up = key_up
      self.key_down = key_down
      self.key_boost = key_boost
      self.facing = facing
      self.color = color
      self.status = status
      self.direction = direction


  #xposes = cls.deque([])
  #yposes = cls.deque([])
  first = blocks(200,200,1,2,20,(cls.deque([])),cls.deque([]),pygame.K_LEFT,pygame.K_RIGHT,pygame.K_UP,pygame.K_DOWN,pygame.K_SPACE,'right',(225,0,0),True,p1bike_right)
  second = blocks(200,200,1,2,20,(cls.deque([])),cls.deque([]),pygame.K_a,pygame.K_d,pygame.K_w,pygame.K_s,pygame.K_e,'left',(0,0,225),True,p1bike_left)
  running = True
  while running == True:
      pygame.time.delay(10)
      screen.fill((0,0,0))
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              running = False

        

      players(first)
      players(second)
      if first.status == False:
        print('player 2 wins')
        pygame.draw.rect(screen,(0,225,0),(second.posx+5,second.posy+5,10,10))
        pygame.time.delay(1000)
        running = False
      if second.status == False:
        pygame.draw.rect(screen,(0,225,0),(first.posx+5,first.posy+5,10,10))
        print ('player 1 wins')
        pygame.time.delay(1000)
        running = False
      pygame.display.update()

      pygame.display.update()
  #pygame.quit()
#Tron()


###########################################################################
#pygame.quit()

##  global facing
##  import pygame
##  import numpy
##  import collections as cls
##
##
##  pygame.init()
##
##  screen = pygame.display.set_mode((600,500))
##   
##  start_ticks=pygame.time.get_ticks()
##  start_ticks2=pygame.time.get_ticks()
##  facing = 'right'
##  length = 10
##  p1bike_up = pygame.image.load('p1_up.jpeg')
##  p1bike_down =pygame.image.load('p1_down.jpeg')
##  p1bike_left =pygame.image.load('p1_left.jpeg')
##  p1bike_right =pygame.image.load('p1_right.jpeg')
##  crash = pygame.image.load('crash.gif')
##  runningtest = True
##  class projectiles:
##    def __init__(self, posx, posy, vel, size):
##      self.posx = posx
##      self.posy = posy
##      self.vel = vel
##      self.size = size
##  def players(self):
##      global facing
##      
##      keys=pygame.key.get_pressed()
##      if keys[self.key_boost]:
##        self.vel = 2
##      else:
##        self.vel = 2
##      if keys[self.key_left] and self.facing!= 'right' and self.facing!='left':
##        self.posx-=self.vel
##        self.facing = 'left'
##      elif keys[self.key_right] and self.facing!= 'left' and self.facing!='right':
##        self.posx+=self.vel
##        self.facing = 'right'
##      elif keys[self.key_down] and self.facing!= 'down' and self.facing!='up':
##        self.posy+=self.vel
##        self.facing = 'down'
##      elif keys[self.key_up] and self.facing!='up' and self.facing !='down':
##        self.posy-=self.vel
##        self.facing = 'up'
##
##      elif self.facing == 'left':
##        self.posx-=self.vel
##        self.direction = p1bike_left
##
##      elif self.facing == 'right':
##        self.posx+=self.vel
##        self.direction = p1bike_right
##      
##      elif self.facing == 'down':
##        self.posy+=self.vel
##        self.direction = p1bike_down
##
##      elif self.facing == 'up':
##        self.posy-=self.vel
##        self.direction = p1bike_up
##
##      if self.posx < 0:
##        self.posx = 590
##        print ('crashed')
##        
##      elif self.posy < 0:
##        self.posy = 490
##        print ('crashed')      
##      elif self.posx > 590:
##        self.posx = 0
##        print ('crashed')
##      elif self.posy > 490:
##        self.posy = 0
##        print ('crashed')
##      
##      k=-1
##      
##      try:
##        while 1-k != len(self.xposes):
##          pygame.draw.rect(screen,self.color,(self.xposes[k],self.yposes[k],5,5))
##          k-=1
##          length=1
##      except:
##        print('not')
##      try: 
##        #if len(self.xposes)>2:
##          j = len(self.xposes)-2
##          while j != 2 :
##            if first.xposes[j]==(self.posx+(self.size/2)) and first.yposes[j] == (self.posy+(self.size/2)):
##                print ('crashed')
##                self.status = False
##                
##                #break
##            if second.xposes[j]==(self.posx+(self.size/2)) and second.yposes[j] == (self.posy+(self.size/2)):
##                print ('crashed')
##                self.status = False
##                #break
##            j-=1
##      except:
##        print('just wait')
##      self.xposes.append(self.posx+(first.size/2))
##      self.yposes.append(self.posy+(first.size/2))
##      screen.blit(self.direction, (self.posx+7,self.posy+7 ))
##      #pygame.draw.rect(screen,self.color,(self.posx,self.posy,self.size,self.size))
##
##  class blocks:
##    def __init__(self, posx, posy, number, vel, size, xposes,yposes,key_left,key_right,key_up,key_down,key_boost,facing,color,status,direction):
##      self.posx = posx
##      self.posy = posy
##      self.number = number
##      self.vel = vel
##      self.size = size
##      self.xposes = xposes
##      self.yposes = yposes
##      self.key_left = key_left
##      self.key_right = key_right
##      self.key_up = key_up
##      self.key_down = key_down
##      self.key_boost = key_boost
##      self.facing = facing
##      self.color = color
##      self.status = status
##      self.direction = direction
##
##
##  #xposes = cls.deque([])
##  #yposes = cls.deque([])
##  first = blocks(200,200,1,1,20,(cls.deque([])),cls.deque([]),pygame.K_LEFT,pygame.K_RIGHT,pygame.K_UP,pygame.K_DOWN,pygame.K_SPACE,'right',(225,0,0),True,p1bike_right)
##  second = blocks(200,200,1,1,20,(cls.deque([])),cls.deque([]),pygame.K_a,pygame.K_d,pygame.K_w,pygame.K_s,pygame.K_e,'left',(0,0,225),True,p1bike_left)
##  running = True
##  while running == True:
##      pygame.time.delay(5)
##      screen.fill((0,0,0))
##      for event in pygame.event.get():
##          if event.type == pygame.QUIT:
##              running = False
##
##        
##
##      players(first)
##      players(second)
##      if first.status == False:
##        print('player 2 wins')
##        screen.blit(crash,(first.posx+5,first.posy+5))
##        pygame.draw.rect(screen,(0,225,0),(second.posx+5,second.posy+5,10,10))
##        runningtest = False
##
##        
##      if second.status == False:
##        pygame.draw.rect(screen,(0,225,0),(first.posx+5,first.posy+5,10,10))
##        print ('player 1 wins')
##        screen.blit(crash,(second.posx+5,second.posy+5))
##        runningtest = False
##
##  
##      pygame.display.update()
##      if runningtest == False:
##          if first.status == False:
##              screen.blit(crash,(first.posx+5,first.posy+5))
##              pygame.display.update()
##          elif second.status == False:
##              screen.blit(crash,(second.posx+5,second.posy+5))
##              pygame.display.update()
##          pygame.time.delay(3000)
##          running = False
##
##  pygame.quit()
Tron()


