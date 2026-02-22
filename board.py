import pygame
import configs
from cell import Cell

class Board(pygame.sprite.Sprite):

    def __init__(self, left = 40, top = 40):
        pygame.sprite.Sprite.__init__(self)
        self.left = left
        self.top = top
        self.texture = pygame.transform.scale2x(pygame.image.load("assets/board.png"))
        self.size = self.texture.get_width()
        self.rect = self.texture.get_rect()
        self.cells = pygame.sprite.Group()
        self.cells.add(*[Cell(i*configs.CELL_SIZE, j*configs.CELL_SIZE) for i in range(9) for j in range(9)])
        self.border = pygame.Rect((left, top, self.size, self.size))

        self.overlay = pygame.Surface(self.rect.size, pygame.SRCALPHA)
        self.image = pygame.Surface(self.rect.size)

    def draw(self, screen):
        pygame.draw.rect(self.overlay, (0, 0, 0, 0), self.rect)
        for cell in self.cells:
            mouse_pos = pygame.mouse.get_pos()
            if cell.rect.collidepoint(mouse_pos[0]-configs.CELL_SIZE/2, mouse_pos[1]-configs.CELL_SIZE/2):
                cell.image.fill(configs.CELL_HIGHLIGHT_COLOR)
                pygame.draw.rect(cell.image, configs.CELL_BORDER_COLOR, cell.border, configs.CELL_BORDER_WIDTH)
            else:
                cell.image.fill(configs.CELL_COLOR)
                pygame.draw.rect(cell.image, configs.CELL_BORDER_COLOR, cell.border, configs.CELL_BORDER_WIDTH)

        self.cells.update()
        self.cells.draw(self.overlay)

        for i in range(1, 3):
            pygame.draw.line(self.overlay, configs.CELL_BORDER_COLOR, (configs.CELL_SIZE*i*3, 0), (configs.CELL_SIZE*i*3, 1000), configs.GRID_BORDER)
            pygame.draw.line(self.overlay, configs.CELL_BORDER_COLOR, (0, configs.CELL_SIZE*i*3), (1000, configs.CELL_SIZE*i*3), configs.GRID_BORDER)
        self.image.fill('black')
        self.image.blit(self.texture)
        self.image.blit(self.overlay)
        screen.blit(self.image, (40, 40))
        pygame.draw.rect(screen, configs.CELL_BORDER_COLOR, self.border, configs.BOARD_BORDER_WIDTH)