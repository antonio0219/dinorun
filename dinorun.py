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
vel = 5
nextFloor = floor[0].getWidth()
squareX = 166

#created objects
player = dino.dinosaur(pygame)


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
        player.jump()
        player.draw(surface)
    if gameState == 1:
        for i in floor:
            i.draw(surface)
        pygame.draw.rect(surface,(255,255,255),(squareX,0,windowWidth,windowHeight))
        player.draw(surface)
        if squareX >= windowWidth:
            gameState = 2
        else:
            squareX += 5
    if gameState == 2:
        for i in floor:
            i.draw(surface)
            i.move(vel)
            i.another(windowWidth)
            if i.another(windowWidth):
                i.mensageReceived()
                floor.append((background.background(pygame, 'floor2', (i.x + i.getWidth()), 200)))
                floor.append((background.background(pygame, 'floor1', (i.x + i.getWidth() + 116), 200)))
        player.jump()
        player.draw(surface)
        
    for event in GAME_EVENTS.get():
        if event.type == GAME_GLOBALS.QUIT:
            quitGame()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.letsJump()
                if gameState == 0:
                    gameState = 1
                    floor.append((background.background(pygame, 'floor1', 50 + nextFloor, 200)))
        
                
        
    clock.tick(60)
    pygame.display.update()
    
    