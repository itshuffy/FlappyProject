#Jesse Huff
#CTI 110
#12/7/2017
#Flappy Bird Final Project

import pygame
from random import randint



#Define Colors - RGB
black = (0,0,0)
white = (255,255,255)
green = (0,255,20)
red = (255,0,0)

pygame.init()

#Screen Size
size = 700,500
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Flappy Bird")

done = False
clock = pygame.time.Clock()
background_image = pygame.image.load("BG.PNG").convert()

def ball(x,y):
    #Radius of 20 px
    pygame.draw.circle(screen,black,[x,y],20)

def gameover():
    font = pygame.font.SysFont(None,55)
    text = font.render("Game Over! Try Again",True,red)
    screen.blit(text, [150,250])

def obstacle(xloc,yloc,xsize,ysize):
    pygame.draw.rect(screen,green,[xloc,yloc,xsize,ysize])
    pygame.draw.rect(screen,green,[xloc,int(yloc+ysize+space),xsize,ysize+500])

#If the ball is between 2 points on the screen, update score
def Score(score):
    font = pygame.font.SysFont(None,55)
    text = font.render("Score: "+str(score),True,black)
    screen.blit(text, [0,0])

x = 350
y = 250
x_speed = 0
y_speed = 0
ground = 477
xloc = 700
yloc = 0
xsize = 70
ysize = randint(0,350)
#Size of space between 2 blocks
space = 150
obspeed = 2
score = 0


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y_speed = -10

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                y_speed = 5
                        
   #Background
    screen.blit(background_image,[0,0])
    obstacle(xloc,yloc,xsize,ysize)
    ball(x,y)
    Score(score)

    y += y_speed
    xloc -= obspeed

    if y > ground:
        gameover()
        y_speed = 0
        obspeed = 0

    if x+20 > xloc and y-20 < ysize and x-15 < xsize+xloc:
        gameover()
        y_speed = 0
        obspeed = 0

    if x+20 > xloc and y+20 < ysize and x-15 < xsize+xloc:
        gameover()
        y_speed = 0
        obspeed = 0

    if xloc < -80:
        xloc = 700
        ysize = randint(0,350)

    if x > xloc and x < xloc+3:
        score = score + 1

    if obspeed < .1:
        gameover()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
