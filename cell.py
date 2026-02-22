import pygame
import configs

class Cell(pygame.sprite.Sprite):

    def __init__(self, left, top):
        pygame.sprite.Sprite.__init__(self)
        self.size = configs.CELL_SIZE
        self.left = left
        self.top = top
        self.image = pygame.surface.Surface((self.size, self.size), pygame.SRCALPHA)
        self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.image.fill(configs.CELL_COLOR)
        self.rect.center = (left, top)
        pygame.draw.rect(self.image, configs.CELL_BORDER_COLOR, (0, 0, self.size, self.size), configs.CELL_BORDER_WIDTH)