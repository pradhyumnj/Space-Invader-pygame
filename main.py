import pygame
from pygame.constants import K_LEFT

# Mandatory initialization 
pygame.init()

# Set Screen size
screenX = 800
screenY = 600
screen = pygame.display.set_mode((screenX, screenY))

# Set Window title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Initializing Player
playerImg = pygame.image.load('spaceship.png')
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0

# Draw player
def player(x,y):
    screen.blit(playerImg, (x, y)) 

#Game loop
running = True
while running:
    # Screen color
    screen.fill((0,0,0))

    # For quitting
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Move player
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                playerX_change -= 1
            if event.key == pygame.K_d:
                playerX_change += 1
            if event.key == pygame.K_w:
                playerY_change -= 1
            if event.key == pygame.K_s:
                playerY_change += 1
        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_d, pygame.K_a):
                playerX_change = 0  
            if event.key in (pygame.K_w, pygame.K_s):   
                playerY_change = 0    
    
    # Update player coordinates
    
    playerX += playerX_change
    playerY += playerY_change
    if playerX < 0:
        playerX = 0
    if playerY < 0:
        playerY = 0
    if playerX > screenX - 64:
        playerX = screenX - 64
    if playerY < 0:
        playerY = 0
    if playerY > screenY - 64:
        playerY = screenY - 64
    player(playerX,playerY)
    pygame.display.update()
