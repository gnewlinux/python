#! /usr/bin/env python
import pygame
from pygame.locals import *
from sys import exit

pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32)

pygame.display.set_caption('Hello World')

count = 0
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    count += 1
    print count
    screen.blit(pygame.Surface(screen.get_size()), (0, 0))
    pygame.display.update()
    time_passed = clock.tick(30)
