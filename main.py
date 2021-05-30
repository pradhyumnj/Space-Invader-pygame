import pygame
from pygame.constants import K_LEFT

# Mandatory initialization 
pygame.init()

# Set Screen
screenX = 800
screenY = 600
background = pygame.image.load('background.png')
screen = pygame.display.set_mode((screenX, screenY))

# Set Window title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Initializing Player
playerImg = pygame.image.load('spaceship.png')
playerX = 370
playerY = 480
delta = 3
playerX_change = 0
playerY_change = 0

# Initializing Ememy
enemyImg = pygame.image.load('spaceship2.png')
enemyX = 370
enemyY = 64
enemyX_change = 0
enemyY_change = 0

# Draw player
def player(x,y):
    screen.blit(playerImg, (x, y))
 
# Draw Enemy
def enemy(x,y):
    screen.blit(enemyImg, (x, y))


#Game loop
running = True
while running:
    # Screen color and background
    screen.fill((0,0,0))
    screen.blit(background,(0,0 ))
    # For quitting
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Move player
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                playerX_change -= delta
            if event.key == pygame.K_d:
                playerX_change += delta
            if event.key == pygame.K_w:
                playerY_change -= delta
            if event.key == pygame.K_s:
                playerY_change += delta
        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_d, pygame.K_a):
                playerX_change = 0  
            if event.key in (pygame.K_w, pygame.K_s):   
                playerY_change = 0   

        # Move Enemy
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                enemyX_change -= delta
            if event.key == pygame.K_RIGHT:
                enemyX_change += delta
            if event.key == pygame.K_UP:
                enemyY_change -= delta
            if event.key == pygame.K_DOWN:
                enemyY_change += delta
        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_RIGHT, pygame.K_LEFT):
                enemyX_change = 0  
            if event.key in (pygame.K_UP, pygame.K_DOWN):   
                enemyY_change = 0     
    
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

    # Update Enemy coordinates
    enemyX += enemyX_change
    enemyY += enemyY_change
    if enemyX < 0:
        enemyX = 0
    if enemyY < 0:
        enemyY = 0
    if enemyX > screenX - 64:
        enemyX = screenX - 64
    if enemyY < 0:
        enemyY = 0
    if enemyY > screenY - 64:
        enemyY = screenY - 64
    enemy(enemyX,enemyY)
    pygame.display.update()
