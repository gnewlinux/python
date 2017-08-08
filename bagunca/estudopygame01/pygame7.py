#! /usr/bin/env python
import pygame
from pygame.locals import *
from sys import exit
from random import randrange

pygame.init()

screen = pygame.display.set_mode((956, 560), 0, 32)

pygame.display.set_caption('Asteroids')

background_filename = 'bg_big.png'
background = pygame.image.load(background_filename).convert()

ship_filename = 'ship.png'
ship = pygame.image.load(ship_filename).convert_alpha()
ship_position = [randrange(956), randrange(560)]

clock = pygame.time.Clock()

def create_asteroid():
    return {
        'surface': pygame.image.load('asteroid.png').convert_alpha(),
        'position': [randrange(892), -64],
        'speed': randrange(1, 11)
    }

def move_asteroids():
    for asteroid in asteroids:
        asteroid['position'][1] += asteroid['speed']

def remove_used_asteroids():
    for asteroid in asteroids:
        if asteroid['position'][1] > 500:
            asteroids.remove(asteroid)

ticks_to_asteroid = 90
asteroids = []

while True:
    
    if not ticks_to_asteroid:
        ticks_to_asteroid = 90
        asteroids.append(create_asteroid())
    else:
        ticks_to_asteroid -= 1

    speed = {
            'x':0,
            'y':0
            }
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    pressed_keys = pygame.key.get_pressed()

    if pressed_keys[K_UP]:
        speed['y'] = -5
    elif pressed_keys[K_DOWN]:
        speed['y'] = 5
    if pressed_keys[K_LEFT]:
        speed['x'] = -5
    elif pressed_keys[K_RIGHT]:
        speed['x'] = 5

    screen.blit(background, (0, 0))
    #ship_position[0] += speed
    ship_position[0] += speed['x']
    ship_position[1] += speed['y']
    screen.blit(ship, ship_position)
    move_asteroids()

    for asteroid in asteroids:
        screen.blit(asteroid['surface'], asteroid['position'])
    pygame.display.update()
    time_passed = clock.tick(30)

    remove_used_asteroids()
