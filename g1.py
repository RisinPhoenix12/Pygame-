import pygame

pygame.init()

win = pygame.display.set_mode((1080,960))

pygame.display.set_caption("First Game")

x =100
y=100
w=80
h=120
v=10

run= True

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x>0 :
        x-=v 
    
    if keys[pygame.K_RIGHT] and x< 1080-w:
        x+=v
    
    if keys[pygame.K_UP] and y>0 :
        y-=v 
    
    if keys[pygame.K_DOWN] and y<960-h:
        y+=v
    
    win.fill((160,160,160))
    pygame.draw.rect(win, (125,125,125), (x,y,w,h))
    pygame.display.update()

pygame.quit()

    
    




