#! /usr/bin/env python
import pygame
from pygame.locals import *
from sys import exit
from random import randrange

## Inicio Pygame
pygame.init()
## Inicio Fonts
pygame.font.init()
## Inicio Sound
pygame.mixer.pre_init(44100, 32, 2, 4096)

## Configuracoes Fontes
font_name = pygame.font.get_default_font()
game_font = pygame.font.SysFont(font_name, 72)
game_font_pontos = pygame.font.SysFont(font_name, 24)

## Configuracao tela principal
screen = pygame.display.set_mode((956, 560), 0, 32)

## Titulo
pygame.display.set_caption('Asteroids')

## Background
background_filename = 'bg_big.png'
background = {
        'surface': pygame.image.load(background_filename).convert(),
        'position': [(0),(-4400)],
        'speed': [(0),(0)]
}

## Importacao Audio explosao
explosion_sound = pygame.mixer.Sound('boom.wav')
explosion_played = False


## --- VARIAVEIS ---

ticks_to_asteroid = 30
clock = pygame.time.Clock()
asteroids = []
collided = False
collision_animation_counter = 0
conti = 60
pontos = 0
restart = 1


## --- OBJETOS ---

ship = {
    'surface': pygame.image.load('ship.png').convert_alpha(),
    'position': [(440),(400)],
    'speed': {
        'x': 0,
        'y': 0
        }
}

exploded_ship = {
    'surface': pygame.image.load('ship_exploded.png').convert_alpha(),
    'position': [],
    'speed': {
        'x': 0,
        'y': 0
     },
     'rect': Rect(0, 0, 48, 48)
}

gun = {
    'surface': pygame.image.load('gun.png').convert_alpha(),
    'position': [(200),(200)],
    'speed': 0,
    'rect': Rect(0, 0, 4, 19)
}


## --- FUNCOES ---

def create_asteroid():
    return {
        'surface': pygame.image.load('asteroid.png').convert_alpha(),
        'position': [randrange(892), -64],
        'speed': randrange(5, 15)
    }

def create_gun():
    return {
        'surface': pygame.image.load('gun.png').convert_alpha(),
        'position': ship['position'],
        'speed': 10
    }

def move_asteroids():
    for asteroid in asteroids:
        asteroid['position'][1] += asteroid['speed']

def remove_used_asteroids():
    global pontos
    for asteroid in asteroids:
        if asteroid['position'][1] > 600:
            asteroids.remove(asteroid)
            pontos += 1

def get_rect(obj):
        return Rect(obj['position'][0],
                obj['position'][1],
                obj['surface'].get_width(),
                obj['surface'].get_height())

def ship_collided():
    ship_rect = get_rect(ship)
    for asteroid in asteroids:
        if ship_rect.colliderect(get_rect(asteroid)):
            return True
    return False


ship['speed'] = {
      'x':0,
      'y':0
}


##### FUNCAO MAIN #####

def main():
       
    global collided
    global ticks_to_asteroid
    global conti
    global pontos

     
    ## LOOP PRINCIPAL / VARIAVEIS / CONTADOR
    while True:
        nave_x = ship['position'][0]
        nave_y = ship['position'][1]
        create_asteroid()
        if not ticks_to_asteroid:
            ticks_to_asteroid = conti
            asteroids.append(create_asteroid())
            conti -= 1
            if conti <= 7:
                conti = 7
        else:
             ticks_to_asteroid -= 1

    ## EXIT ON
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()

    ## BACKGROUND / NAVE

        background['position'][1] += 0.8
        screen.blit(background['surface'], background['position'])
   
        ship['surface'] = pygame.image.load('ship.png').convert_alpha()
   
   
   ## KEY LIST
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[K_UP]:
            ship['speed']['y'] -= 0.5
            ship['surface'] = pygame.image.load('ship_f.png').convert_alpha()
        elif pressed_keys[K_DOWN]:
            ship['speed']['y'] += 0.5
        if pressed_keys[K_LEFT]:
            ship['speed']['x'] -= 0.5
            ship['surface'] = pygame.image.load('ship_e.png').convert_alpha()
        elif pressed_keys[K_RIGHT]:
            ship['speed']['x'] += 0.5
            ship['surface'] = pygame.image.load('ship_d.png').convert_alpha()
        elif pressed_keys[K_SPACE]:
            #gun['position'][1] += 1
            #screen.blit(gun['surface'], ship['position'])
            create_gun()
        elif pressed_keys[K_ESCAPE]:
            exit()


    ## GRAVIDADE
        if ship['speed']['x'] < 0:
            ship['speed']['x'] += 0.1
   
        if ship['speed']['y'] < 0:
            ship['speed']['y'] += 0.1
  
        if ship['speed']['x'] > 0:
            ship['speed']['x'] -= 0.1
   
        if ship['speed']['y'] > 0:
            ship['speed']['y'] -= 0.1

    ## FIM DO MAPA
        if ship['position'][1] > 590:
            ship['position'][1] = -20
        if ship['position'][1] < -30:
            ship['position'][1] = 580
    
        if ship['position'][0] > 980:
            ship['position'][0] = -20
        if ship['position'][0] < -30:
            ship['position'][0] = 970


        if not collided:
            collided = ship_collided()
            ship['position'][0] += ship['speed']['x']
            ship['position'][1] += ship['speed']['y']

            ponto = game_font_pontos.render(str(pontos), 1, (255,255,255))
            screen.blit(ponto, (910,520))
            contador = game_font_pontos.render('PONTOS', 1, (255,255,255))
            screen.blit(contador, (820,520))
        
            screen.blit(ship['surface'], ship['position'])
    
        else:
            
            global explosion_played
            global collision_animation_counter
            if not explosion_played:
                explosion_played = True
                explosion_sound.play()
                ship['position'][0] += ship['speed']['x']
                ship['position'][1] += ship['speed']['y']
                ponto_final = ponto

                screen.blit(ship['surface'], ship['position'])
            elif collision_animation_counter == 3:
                text = game_font.render('GAME OVER', 1, (255,0,0))
                screen.blit(text, (335,250))
                screen.blit(ponto_final, (490,320))
            
                ## RESTART GAME
                if pressed_keys[K_RETURN]:
                    explosion_played = False
                    collided = False
                    collision_animation_counter = 0
                    ship['position'][0] = 440
                    ship['position'][1] = 400
                    ship['speed']['x'] = 0
                    ship['speed']['y'] = 0
                    ponto = 0
                    ponto_final = 0
                    pontos = 0
                    conti = 60
                    main()

            
            else:
                exploded_ship['rect'].x = collision_animation_counter * 48
                exploded_ship['position'] = ship['position']
                screen.blit(exploded_ship['surface'], exploded_ship['position'],
                exploded_ship['rect'])
                collision_animation_counter += 1


    
        move_asteroids()
    

        for asteroid in asteroids:
            screen.blit(asteroid['surface'], asteroid['position'])

        pygame.display.update()
        time_passed = clock.tick(30)

        remove_used_asteroids()

main()
