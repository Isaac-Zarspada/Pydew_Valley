import pygame
from settings import *

class Level:
    def run(self, dt):
        self.display_surface.fill('black')
        self.all_sprites.draw(self.display_surface)
        self.all_sprites.update()
        print('run game')