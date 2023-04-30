import pygame 
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)

        #  character setup
        self.image = pygame.Surface((32,64)) 
        self.image.fill('black')
        self.rect = self.image.get_rect(center = pos)

        # movement attributes
        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 200


    def import_assets():
        pass

    def input(self):
        key = pygame.key.get_pressed()
# up and down movement
        if key[pygame.K_UP]:
            print('up')
            self.direction.y = -1
        elif key[pygame.K_DOWN]:
            print('down')
            self.direction.y = 1
        else:
            self.direction.y=0
# left right movement
        if key[pygame.K_LEFT]:
            print('left')
            self.direction.x = -1
        elif key[pygame.K_RIGHT]:
            print('right')
            self.direction.x = 1
        else:
            self.direction.y=0
        print(self.direction)
    def update(self, dt):
        self.input()
