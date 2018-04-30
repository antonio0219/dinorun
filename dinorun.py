import pygame, sys, random
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS
import pygame.time as GAME_TIME
import dino, obstacles, background

windowWidth = 750
windowHeight = 250

#listas de obstáculos y suelo
floor = [(background.background(pygame, 'floor2', 50, 200))]
clouds = []
cactusAndBirds = []

#variables
gameState = 0
vel = 0
nextFloor = floor[0].getWidth()
print(str(nextFloor))



pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()
surface = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption('DINORUN')

#load images


#música y sonidos


def quitGame(): #para quitar el juego
    pygame.quit()
    sys.exit()
    
while True:
    surface.fill(((255,255,255)))
    if gameState == 0:
        floor[0].draw(surface)
        
    clock.tick(60)
    pygame.display.update()
    
    