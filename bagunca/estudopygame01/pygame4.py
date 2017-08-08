#! /usr/bin/env python
import pygame
from pygame.locals import *
from sys import exit
# from random import randrange

pygame.init()

screen = pygame.display.set_mode((956, 560), 0, 32)

pygame.display.set_caption('Hello World')

background_filename = 'bg_big.png'
background = pygame.image.load(background_filename).convert()

ship_filename = 'ship.png'
ship = pygame.image.load(ship_filename).convert_alpha()
ship_position = [0, 280]
# ship_position = [randrange(956), randrange(560)]
speed = 3

clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    screen.blit(background, (0, 0))
    ship_position[0] += speed
    #ship_position[0] += randrange(-10, 10)
    #ship_position[1] += randrange(-10, 10)
    screen.blit(ship, ship_position)
    pygame.display.update()
    time_passed = clock.tick(30)
