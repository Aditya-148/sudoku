import pygame
import configs
from cell import Cell

class Board(pygame.sprite.Sprite):

    def __init__(self, left = 40, top = 40):
        pygame.sprite.Sprite.__init__(self)
        self.size = 100
        self.left = left
        self.top = top
        self.image = pygame.transform.scale2x(pygame.image.load(r"assets\board.png"))
        self.rect = self.image.get_rect()
        self.cells = pygame.sprite.Group()
        self.cells.add(*[Cell(i*configs.CELL_SIZE+configs.CELL_SIZE//2, j*configs.CELL_SIZE+configs.CELL_SIZE//2) for i in range(9) for j in range(9)])
        print(self.cells)

    def draw(self, screen):
        self.cells.update()
        screen.blit(self.image, (40, 40))
        self.cells.draw(self.image)
    
    def collides(self):
        for cell in self.cells:
            cell.collides
        