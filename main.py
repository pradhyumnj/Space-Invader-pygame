import pygame
from pygame import mixer
import time

# Mandatory initialization 
pygame.init()

# Set Screen
screenX = 800
screenY = 600
background = pygame.image.load('media/background.png')
screen = pygame.display.set_mode((screenX, screenY))

# Set music
mixer.music.load('media/background.wav')
mixer.music.play(-1)
bullet_sound = mixer.Sound('media/laser.wav')
explosion_sound = mixer.Sound('media/explosion.wav')

# Set Window title and icon
pygame.display.set_caption("media/Space Invaders")
icon = pygame.image.load('media/ufo.png')
pygame.display.set_icon(icon)

# Initializing Player
playerImg = pygame.image.load('media/spaceship.png')
playerX = 370
playerY = 480
delta = 3
playerX_change = 0
playerY_change = 0
player_health = 10

# Initializing Ememy
enemyImg = pygame.image.load('media/spaceship2.png')
enemyX = 370
enemyY = 64
enemyX_change = 0
enemyY_change = 0
enemy_health = 10

# Initializing player bullet
bulletImg = pygame.image.load('media/bullet.png')
bulletX = 370
bulletY = 480
bullet_delta = 5
bullet_state = 'ready'

# Initializing enemy bullet
bullet1Img = pygame.image.load('media/bullet1.png')
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

# Game Over 
over = pygame.font.Font('freesansbold.ttf',1000)
def game_over(x = screenX/2 - 200, y = screenY/2):
    game_over_text = font.render(f'Game Over', True, (255,0,0))
    screen.blit(game_over_text, (x,y))


# Displaying health
font = pygame.font.Font('freesansbold.ttf',32)
def p1_health(x = screenX - 190 ,y = screenY - 50):
    health = font.render(f'Health : {player_health}', True, (255,255,255))
    screen.blit(health, (x,y))
def p2_health(x = 10,y = 10):
    health = font.render(f'Health : {enemy_health}', True, (255,255,255))
    screen.blit(health, (x,y))

#Game loop
running = True
while running:

    # Screen color and background
    screen.fill((0,0,0))
    screen.blit(background,(0,0 ))
    # For quitting
    if bullet_state == 'ready':
        bulletY = playerY
        bulletX = playerX
    if bullet1_state == 'ready':
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
                if bullet_state == 'ready':
                    bullet_sound.play()
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
                if bullet1_state == 'ready':
                    bullet_sound.play()
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
    if playerY < screenY/2 + 15:
        playerY = screenY/2 + 15
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
    if enemyY > screenY/2 - 64 - 15:
        enemyY = screenY/2 - 64 - 15
    enemy(enemyX,enemyY)

    #Firing 
    if bullet_state == 'fire':
        fire(bulletX, bulletY)
        bulletY -= bullet_delta
    if bullet1_state == 'fire':
        fire1(bullet1X, bullet1Y)  
        bullet1Y += bullet_delta 
        
    #reloading
    if bulletY < 0:
        bullet_state = 'ready'
    if bullet1Y > screenY:
        bullet1_state = 'ready'

    if ((bulletX-enemyX)**2 + (bulletY-enemyY)**2)**0.5 < 30:
        bullet_state = 'ready'
        explosion_sound.play()
        enemy_health -= 1
    if ((bullet1X-playerX)**2 + (bullet1Y-playerY)**2)**0.5 < 30:
        bullet1_state = 'ready'  
        explosion_sound.play()
        player_health -= 1


    p1_health()
    p2_health()
    i = 0
    if i == 0:
        while (player_health == 0 or enemy_health == 0):
            game_over()
            pygame.display.update()
            i += 1
            if i == 10:
                break
            time.sleep(1)
            exit()
    pygame.display.update()

