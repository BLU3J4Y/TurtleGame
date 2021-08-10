import os
import pygame
from PIL import Image
import time
import animations
import game_var

# Variables



pygame.display.set_caption('Turtle Simulator')
pygame.display.set_icon(game_var.logo64x)

################################################################
#                                                              #
#                   Animations and Cutscenes                   #
#                                                              #
################################################################

# Startup Screen



time.sleep(1)

skip_startup = False
for event in pygame.event.get():
    if event.type == pygame.KEYDOWN and event.key == pygame.K_LSHIFT:
        print('Startup sequence skipped!')
        skip_startup = True

pygame.init() 

animations.startup_sequence(skip_startup)

# Game Loop

while game_var.running:
    
    # Check Game State

    GAME_STATE = game_var.game_state.split('.')

    if GAME_STATE[0] == 'homescreen':
        pygame.time.delay(20)
        animations.home_screen()
        pygame.display.update()
    if GAME_STATE[0] == 'play':
        None