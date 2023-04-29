import pygame
from settings import *
from player import Player

class Level:
    def __init__(self):

        self.display_surface = pygame.display.get_surface()
        self.all_sprites = pygame.sprite.Group()

    def setup(self):
        self.player = Player

    def run(self, dt):
        self.display_surface.fill('red')
        self.all_sprites.draw(self.display_surface)
        self.all_sprites.update()
        print('run game')