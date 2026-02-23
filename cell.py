import pygame
import configs
import random

class Cell(pygame.sprite.Sprite):

    def __init__(self, left, top, value=0):
        pygame.sprite.Sprite.__init__(self)
        self.size = configs.CELL_SIZE
        self.left = left
        self.top = top
        self.image = pygame.surface.Surface((self.size, self.size), pygame.SRCALPHA)
        self.image.convert_alpha()
        self.rect = self.image.get_rect(topleft=(left, top))
        self.image.fill(configs.CELL_COLOR)
        self.border = pygame.Rect((0, 0, self.size, self.size))
        self.value = value