import pygame
from settings import *

class Level:
    def __init__(self):

        self.display_surface = pygame.display.get_surface()
        self.all_sprites = pygame.sprite.Group()



    def run(self, dt):
        print('run game')