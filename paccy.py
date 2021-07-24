import pygame
from ims import img
import time
pygame.init()
class pacman:
    
    #main loop runs continuously and contains the main logic and calling of functions and objects
    def __init__(self,ghostn):

        self.swdth=1920
        self.shgt=1080
        self.stop=False

        #setting basic parameters 
        self.RED = (255,0,0)
        self.BLACK = (0,0,0)
        self.GREEN = (0,255,0)
        self.WHITE = (255,255,255)
        self.fps = 60 
        self.run = True
        self.clock = pygame.time.Clock()
        

        #creating screen
        self.win = pygame.display.set_mode((self.shgt,self.swdth))
        self.win.fill(self.WHITE)
        #modifying displayed screen
        pygame.display.set_caption("MY PAC")
        self.logo =pygame.image.load('logo.jpg')
        pygame.display.set_icon(self.logo)

        self.ghostn = ghostn
        self.objnum = 0

    def sdisplay(self):
        
        self.ghosts = [img()for i in range(self.ghostn)]
        self.ghosts[0].x=10
        for j in range(1,self.ghostn):
            for k in range(0,self.ghostn-j):
                self.ghosts[j].x=(j*self.ghosts[0].w+(j+1)*9)
                if self.ghosts[j].x<(self.swdth-self.ghosts[0].w):
                    self.win.blit(self.ghosts[j].ghosti,(self.ghosts[j].x,self.ghosts[j].y))

                else:
                    self.ghosts[j].x=(self.ghosts[0].w*k)+(k+1)*10
                    self.ghosts[j].y=(self.ghosts[0].h+50)
                    self.win.blit(self.ghosts[j].ghosti,(self.ghosts[j].x,self.ghosts[j].y))


        while self.run:
            self.clock.tick(self.fps)
        
            for event in pygame.event.get():

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.objnum = self.mpt()

                if event.type == pygame.QUIT:
                    self.run = False
                    pygame.quit()
                    quit()


                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.ghosts[self.objnum].xspd=10
        
                    if event.key == pygame.K_LEFT:
                        self.ghosts[self.objnum].xspd=-10

                    if event.key == pygame.K_UP:
                        self.ghosts[self.objnum].yspd=-10

                    if event.key == pygame.K_DOWN:
                        self.ghosts[self.objnum].yspd=+10
        
                if event.type == pygame.KEYUP and (event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT or event.key == pygame.K_UP or event.key == pygame.K_DOWN):
                    self.ghosts[self.objnum].xspd=0
                    self.ghosts[self.objnum].yspd=0
            
            self.ghosts[self.objnum].x=self.ghosts[self.objnum].x+self.ghosts[self.objnum].xspd
            self.ghosts[self.objnum].y=self.ghosts[self.objnum].y+self.ghosts[self.objnum].yspd

            self.win.fill(self.WHITE)

            for i in range(0,self.ghostn):
                if i!=self.objnum:
                    if((self.ghosts[i].x<=self.ghosts[self.objnum].x<=self.ghosts[i].x + self.ghosts[0].w) or (self.ghosts[i].x<=self.ghosts[self.objnum].x + self.ghosts[0].w<=self.ghosts[i].x+self.ghosts[0].w)):
                        if((self.ghosts[i].y<=self.ghosts[self.objnum].y<=self.ghosts[i].y + self.ghosts[0].h) or (self.ghosts[i].y<=self.ghosts[self.objnum].y + self.ghosts[0].h<=self.ghosts[i].y+self.ghosts[0].h)):
                            self.win.fill((self.GREEN))
                    elif((self.ghosts[i].x<self.ghosts[self.objnum].x<self.ghosts[i].x + self.ghosts[0].w) or (self.ghosts[i].x<self.ghosts[self.objnum].x + self.ghosts[0].w<self.ghosts[i].x+self.ghosts[0].w)):
                        if((self.ghosts[i].y<self.ghosts[self.objnum].y<self.ghosts[i].y + self.ghosts[0].h) or (self.ghosts[i].y<self.ghosts[self.objnum].y + self.ghosts[0].h<self.ghosts[i].y+self.ghosts[0].h)):
                            self.win.fill((self.BLACK))
                    
            for j in self.ghosts:
                self.win.blit(j.ghosti,(j.x,j.y))

            pygame.display.update()

    def mpt(self):
        self.c=1
        self.m_posx,self.m_posy=pygame.mouse.get_pos()

        for i in range (0,self.ghostn):
            if (self.ghosts[i].x+self.ghosts[0].w>=self.m_posx>=self.ghosts[i].x and self.ghosts[i].y+self.ghosts[0].h>=self.m_posy>=self.ghosts[i].y):
                self.c=0
                #print(i)
                break

        if(self.c==0):
            return i
                

        elif self.c==1:
              return self.objnum

    
  
    
                


    