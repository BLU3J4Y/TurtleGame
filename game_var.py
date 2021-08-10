import pygame
import os
from PIL import Image

# Display and Window Stuff

window = (1200, 800)
display = pygame.display.set_mode((window[0],window[1]))


# Game Logos

logo500x_dir = os.path.join('','assets/icons/logos/x500.png')
logo500x_dim = Image.open(logo500x_dir).size
logo500x = pygame.image.load(logo500x_dir)

logo64x_dir = os.path.join(''+'assets/icons/logos/x64.png')
logo64x = pygame.image.load(logo64x_dir)


#

hover = []

homescreen_items = {
    "title" : pygame.image.load(os.path.join('assets','adventures_of_mopey_and_robbie_title.png')).convert_alpha(),
    "start_button": pygame.image.load(os.path.join('assets/gui/homescreen','start.png')).convert_alpha(),
    "options_button": pygame.image.load(os.path.join('assets/gui/homescreen','options.png')).convert_alpha()
}

# Game Variables

running = True
game_state = ''

SELECTION = None