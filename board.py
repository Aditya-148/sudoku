import pygame
import configs
from cell import Cell

class Board(pygame.sprite.Sprite):
    pygame.font.init()
    font = pygame.Font(size=configs.FONT_SIZE)

    def __init__(self, left = 40, top = 40):
        pygame.sprite.Sprite.__init__(self)
        values = [8, 2, 7, 1, 5, 4, 3, 9, 6, 
                  9, 6, 5, 3, 2, 7, 1, 4, 8,
                  3, 4, 1, 6, 8, 9, 7, 5, 2,
                  5, 9, 3, 4, 6, 8, 2, 7, 1,
                  4, 7, 2, 5, 1, 3, 6, 8, 9,
                  6, 1, 8, 9, 7, 2, 4, 3, 5,
                  7, 8, 6, 2, 3, 5, 9, 1, 4,
                  1, 5, 4, 7, 9, 6, 8, 7, 3,
                  2, 3, 9, 8, 4, 1, 5, 6, 7,
                  ]
        self.left = left
        self.top = top
        self.texture = pygame.transform.scale2x(pygame.image.load("assets/board.png"))
        self.size = self.texture.get_width()
        self.rect = self.texture.get_rect()
        self.cells = pygame.sprite.Group()
        self.cells.add(*[Cell(i*configs.CELL_SIZE, j*configs.CELL_SIZE, value=values[i+j*9]) for i in range(9) for j in range(9)])
        self.border = pygame.Rect((left, top, self.size, self.size))

        self.overlay = pygame.Surface(self.rect.size, pygame.SRCALPHA)
        self.image = pygame.Surface(self.rect.size)

    def draw(self, screen):
        pygame.draw.rect(self.overlay, (0, 0, 0, 0), self.rect)

        for cell in self.cells:
            cell_overlay = pygame.Surface(cell.rect.size, pygame.SRCALPHA)
            num_surface = self.font.render(str(cell.value), True, "black")
            mouse_pos = pygame.mouse.get_pos()

            if cell.rect.collidepoint(mouse_pos[0]-configs.CELL_SIZE/2, mouse_pos[1]-configs.CELL_SIZE/2):
                cell_overlay.fill(configs.CELL_HIGHLIGHT_COLOR)
                pygame.draw.rect(cell.image, configs.CELL_BORDER_COLOR, cell.border, configs.CELL_BORDER_WIDTH)
            else:
                cell.image.fill(configs.CELL_COLOR)
                pygame.draw.rect(cell.image, configs.CELL_BORDER_COLOR, cell.border, configs.CELL_BORDER_WIDTH)
            cell.image.blit(num_surface, ((configs.CELL_SIZE-num_surface.size[0])//2, (configs.CELL_SIZE-num_surface.size[1])//2))
            cell.image.blit(cell_overlay)
            

        self.cells.update()
        self.cells.draw(self.overlay)

        for i in range(1, 3):
            pygame.draw.line(self.overlay, configs.CELL_BORDER_COLOR, (configs.CELL_SIZE*i*3, 0), (configs.CELL_SIZE*i*3, 1000), configs.GRID_BORDER)
            pygame.draw.line(self.overlay, configs.CELL_BORDER_COLOR, (0, configs.CELL_SIZE*i*3), (1000, configs.CELL_SIZE*i*3), configs.GRID_BORDER)

        self.image.blit(self.texture)
        self.image.blit(self.overlay)
        screen.blit(self.image, (40, 40))
        pygame.draw.rect(screen, configs.CELL_BORDER_COLOR, self.border, configs.BOARD_BORDER_WIDTH)

    def validate(self):
        cell_list = self.cells.sprites()

        # validate columns
        # for i in range(9):
        #     hash = set()
        #     for j in range(9):
        #         if cell_list[j+i*9].value in hash:
        #             return False
        #         else:
        #             hash.add(cell_list[j+i*9].value)

        # # validate rows
        # for i in range(9):
        #     hash = set()
        #     for j in range(9):
        #         if cell_list[i+j*9].value in hash:
        #             return False
        #         else:
        #             hash.add(cell_list[i+j*9].value)

        # validate grids
        i = 0
        j = 0
        check_grid = True
        while check_grid:
            if j % 3 == 0:
                hash = set()
            for n in range(3):
                if cell_list[(i+n)+j*9].value in hash:
                    return False
                else:
                    hash.add(cell_list[(i+n)+j*9].value)
                if (i+n)+j*9 == 80:
                    check_grid = False
            j += 1
            if j % 9 == 0:
                j = 0
                i += 3
            
        return True