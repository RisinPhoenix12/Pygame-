import pygame
import time
from paccy import pacman
from ims import img

pygame.init()

if __name__=="__main__":
    
    k=int(input("Enter number of ghosts: "))
    paccyman=pacman(k)
    paccyman.sdisplay()