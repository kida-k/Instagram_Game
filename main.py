import sys

import pygame
import os
from pygame.locals import QUIT

score = 0


def ball_animation():
    global ball_speed_x, ball_speed_y, score, score_increment  # Declare intent to modify global variables
    if ball.colliderect(player):
        ball_speed_y *= -1
    
       # ball.x = player.right
        score += score_increment
        
    if (ball.bottom + 30 >= player.x): 
        ball.x += ball_speed_x
    if ball.bottom + 30 >= player.y: 
        ball.y += ball_speed_y
        
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    
    
    
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
        #ball_restart()
    if ball.left <= 0 or ball.right >= screen_width:
        ball_speed_x*=-1
    
    if ball.bottom >= screen_width:
        ball_restart() 
        
        
    
    # if ball bottom end game
    
def player_animation():
    player.x += player_speed
    if player.left <= 0:
        player.left = 0
    if player.right >= screen_width:
        player.right = screen_width
        
def ball_restart():
    global score
    ball.center = (screen_width // 2, screen_height // 2)
    score = 0


    

pygame.init()
pygame.font.init()
clock = pygame.time.Clock() 
player_speed = 0
score_increment = 1
ball_speed_x = 7
ball_speed_y= 7
screen_width = 650
screen_height = 650

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Insta Game uwu')

ball = pygame.Rect(screen_width/2-15,screen_height/2-300,30,30)
player = pygame.Rect(screen_width/2-1-50,screen_height/2+300,140,10)

bg_color = pygame.Color('grey12')
light_grey=(200,200,200)





while True:
    for event in pygame.event.get():
        # collision 
        # ballphysics
        # PlayerMovement
        # Score
   
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player_speed += 7
            if event.key == pygame.K_LEFT:
                player_speed += -7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                player_speed += -7
            if event.key == pygame.K_LEFT:
                player_speed += 7
    #if player.colliderect(ball):
        #score += score_increment
           

    
    ball_animation()
    player_animation()
   
    screen.fill(bg_color)     
    pygame.draw.rect(screen,light_grey,player)     
    pygame.draw.ellipse(screen,light_grey,ball)

    
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", True, light_grey)
    screen.blit(text, (10, 10))
    
    pygame.display.flip()
    clock.tick(32)

