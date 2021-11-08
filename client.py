import pygame
import math

pygame.init()
displaywidth = 900
displayheight = 900
screen = pygame.display.set_mode((displaywidth, displayheight))

pygame.display.set_caption("Multiplayer Game")

playerImg = pygame.image.load('player.png')
x = 50
y = 50
width = 64
height = 64
basespeed = 2
boostmodifier = 2
boostspeed = basespeed * boostmodifier
vel = basespeed

def player():
    screen.blit(playerImg,(x,y))
    pygame.display.update()

running = True
while running:
    #frame rate: 7 = about 142.9 fps, 17 = about 58.8 fps, 10 = exactly 100 fps
    pygame.time.delay(10)
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    buttons = pygame.key.get_pressed()

    if buttons[pygame.K_LEFT] and x > vel:
        x -= vel
    if buttons[pygame.K_RIGHT] and x < displaywidth - width + vel:
        x += vel
    if buttons[pygame.K_UP] and y > vel:
        y -= vel
    if buttons[pygame.K_DOWN] and y < displaywidth - height - vel:
        y += vel
    if buttons[pygame.K_SPACE]:
        vel = boostspeed
    else:
        vel = basespeed

    player()
   
pygame.quit()