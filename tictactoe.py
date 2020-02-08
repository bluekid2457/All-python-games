def tic():
    global turn
    global allcounts
    global running
    global running
    import pygame
    import collections as cls
    
    def board():
        pygame.draw.rect(screen,(225,225,225),(197,0,6,600))
        pygame.draw.rect(screen,(225,225,225),(397,0,6,600))
        pygame.draw.rect(screen,(225,225,225),(0,197,600,6))
        pygame.draw.rect(screen,(225,225,225),(0,397,600,6))
    class spots:
        def __init__(self, posxmin, posxmax, posymin, posymax, possession,num):
            self.posxmin = posxmin
            self.posxmax = posxmax
            self.posymin = posymin
            self.posymax = posymax
            self.possession = possession
            self.num = num 
    class players:
        def __init__(self,name,spots,color):
            self.name = name
            self.spots = spots
            self.color = color

    p1 = players('p1',cls.deque([]),(225,0,0))
    p2 = players('p2',cls.deque([]),(0,0,225))
    turn = 1
    allcounts = 0

    spaces = [1,2,3,4,5,6,7,8,9]
##    p1_spaces=[]
##    p2_spaces=[]
    
    s1 = spots(0,200,0,200,'null',1)
    s2 = spots(201,400,0,200,'null',2)
    s3 = spots(401,600,0,200,'null',3)
    
    s4 = spots(0,200,201,400,'null',4)
    s5 = spots(201,400,201,400,'null',5)
    s6 = spots(401,600,201,400,'null',6)

    s7 = spots(0,200,401,600,'null',7)
    s8 = spots(201,400,401,600,'null',8)
    s9 = spots(401,600,401,600,'null',9)


    def choosing(player):
        global turn
        #if event.type == pygame.MOUSEBUTTONDOWN:
        pos = pygame.mouse.get_pos()
        for k in [s1,s2,s3,s4,s5,s6,s7,s8,s9]:
            if pos[0] > k.posxmin  and pos[0] < k.posxmax and pos[1] > k.posymin and pos[1] < k.posymax:
                pygame.draw.rect(screen,player.color,(k.posxmin,k.posymin,197,197))
                if event.type == pygame.MOUSEBUTTONDOWN and k.possession == 'null':
                    k.possession = player.name
                    (player.spots).append(k.num)
                    turn+=1
    def coloring():                
        for p in [p1,p2]:                
            for l in [s1,s2,s3,s4,s5,s6,s7,s8,s9]:
                if l.possession == p.name:
                    pygame.draw.rect(screen,p.color,(l.posxmin,l.posymin,197,197))
                    
    def checkwin(p):
         global allcounts
         global running

         for a in ((1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)):
             allcounts=0
             for j in a:
                 #print(a)
                 if (p.spots).count(j) == 1:
                     allcounts +=1
                     
             if allcounts == 3:
                 screen.fill(p.color)
                 pygame.display.update()
                 pygame.time.delay(1000)
                 running = False
    pygame.init()
    screen = pygame.display.set_mode((600,600))
    running = True
    while running == True:
        #global running
        pygame.time.delay(10)
        screen.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        board()
        if turn%2 == 0:
            choosing(p1)


        elif turn%2 == 1:
            choosing(p2)
        coloring()            
        checkwin(p1)
        checkwin(p2)

        pygame.display.update()
    #pygame.quit()
#tic()
