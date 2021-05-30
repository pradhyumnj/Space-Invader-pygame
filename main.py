import pygame
#from pygame.constants import K_LEFT

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
player_score = 0

# Initializing Ememy
enemyImg = pygame.image.load('spaceship2.png')
enemyX = 370
enemyY = 64
enemyX_change = 0
enemyY_change = 0
enemy_score = 0

# Initializing player bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = 370
bulletY = 480
bullet_delta = 5
bullet_state = 'ready'

# Initializing enemy bullet
bullet1Img = pygame.image.load('bullet1.png')
bullet1X = 370
bullet1Y = 64
bullet1_state = 'ready'

# Draw player
def player(x,y):
    screen.blit(playerImg, (x, y))
 
# Draw Enemy
def enemy(x,y):
    screen.blit(enemyImg, (x, y))

# Fire player bullet
def fire(x, y):
    global bullet_state
    bullet_state = 'fire' 
    screen.blit(bulletImg, (x+16, y+10))

def fire1(x, y):
    global bullet1_state
    bullet1_state = 'fire'   
    screen.blit(bullet1Img, (x+16, y+10))

#Game loop
running = True
while running:
    # Screen color and background
    screen.fill((0,0,0))
    screen.blit(background,(0,0 ))
    # For quitting
    if bullet_state is 'ready':
        bulletY = playerY
        bulletX = playerX
    if bullet1_state is 'ready':
        bullet1Y = enemyY
        bullet1X = enemyX

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
            if event.key == pygame.K_SPACE:
                fire(playerX,playerY)
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
            if event.key == pygame.K_PERIOD:
                fire1(enemyX,enemyY)
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

    #Firing 
    if bullet_state is 'fire':
        fire(bulletX, bulletY)
        bulletY -= bullet_delta
    if bullet1_state is 'fire':
        fire1(bullet1X, bullet1Y)  
        bullet1Y += bullet_delta 
        
    #reloading
    if bulletY < 0:
        bullet_state = 'ready'
    if bullet1Y > screenY:
        bullet1_state = 'ready'

    if ((bulletX-enemyX)**2 + (bulletY-enemyY)**2)**0.5 < 30:
        bullet_state = 'ready'
        player_score += 1
    if ((bullet1X-playerX)**2 + (bullet1Y-playerY)**2)**0.5 < 30:
        bullet1_state = 'ready'   
        enemy_score += 1
    pygame.display.update()
