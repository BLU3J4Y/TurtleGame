import game_var
import time
import pygame
import os
from PIL import Image

def startup_sequence(skip):

    fade = pygame.Surface((game_var.window[0],game_var.window[1]))
    fade.fill((255,255,255))

    if skip == False:
        game_var.display.fill((255,255,255)) # Background
        pygame.display.update()

        for alpha in reversed(range(0,255)):
            fade.set_alpha(alpha)
            game_var.display.blit(game_var.logo500x, ( int((game_var.window[0] - game_var.logo500x_dim[0]) / 2) , int((game_var.window[1] - game_var.logo500x_dim[1]) / 2)  ))
            game_var.display.blit(fade, (0,0))
            pygame.display.update()

        game_var.display.blit(game_var.logo500x, ( int((game_var.window[0] - game_var.logo500x_dim[0]) / 2) , int((game_var.window[1] - game_var.logo500x_dim[1]) / 2)  ))
        pygame.display.update()

        pygame.time.delay(2000)

        for alpha in range(0,255):
            fade.set_alpha(alpha)
            game_var.display.blit(game_var.logo500x, ( int((game_var.window[0] - game_var.logo500x_dim[0]) / 2) , int((game_var.window[1] - game_var.logo500x_dim[1]) / 2)  ))
            game_var.display.blit(fade, (0,0))
            pygame.display.update()
        
    elif skip == True:
        game_var.display.fill((255,255,255)) # Background
        pygame.display.update()

    game_var.display.fill((118,214,195))
    game_var.game_state = 'homescreen'

    time.sleep(1.00)
    
    for alpha in reversed(range(0,255)):
        home_screen()
            
        fade.set_alpha(alpha)
        game_var.display.blit(fade, (0,0))
        pygame.display.update()
    


def home_screen():
    GAME_TITLE = {
        "el" : game_var.homescreen_items['title'],
        "pos" : (256, 100)
        }
    START_BUTTON = {
        "el" : game_var.homescreen_items['start_button'],
        "pos" : (389, 400),
        "dim" : (502, 102)
    }
    OPTIONS_BUTTON = {
        "el" : game_var.homescreen_items['options_button'],
        "pos" : (389, 550),
        "dim" : (502, 102)
        }

    if type(game_var.SELECTION) != int or (game_var.SELECTION < 1 and game_var.SELECTION > 2): game_var.SELECTION = 1

    SELECTIONS = [START_BUTTON,OPTIONS_BUTTON]

    cursor_X = pygame.mouse.get_pos()[0]
    cursor_Y = pygame.mouse.get_pos()[1]

    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:
            cursor_X = event.pos[0]
            cursor_Y = event.pos[1]
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP: game_var.SELECTION = 1 
            elif event.key == pygame.K_DOWN: game_var.SELECTION = 2
            elif event.key == pygame.K_RETURN: 
                if game_var.SELECTION == 1: 
                    game_var.game_state = 'play.game'
                elif game_var.SELECTION == 2: None
        if event.type == pygame.QUIT: game_var.running = False

    if game_var.SELECTION == 1:
        for sel in SELECTIONS: sel['el'].set_alpha(125)
        START_BUTTON['el'].set_alpha(255)
    elif game_var.SELECTION == 2:
        for sel in SELECTIONS: sel['el'].set_alpha(125)
        OPTIONS_BUTTON['el'].set_alpha(255)

    game_var.display.fill((118,214,195))
    game_var.display.blit(GAME_TITLE['el'], GAME_TITLE['pos'])
    game_var.display.blit(START_BUTTON['el'], START_BUTTON['pos'])
    game_var.display.blit(OPTIONS_BUTTON['el'], OPTIONS_BUTTON['pos'])


    