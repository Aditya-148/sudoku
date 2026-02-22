import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True


class Board:

    def __init__(self):

        self.surf = pygame.Surface((540, 540))
        self.surf.fill("chocolate4")
        self.rect = self.surf.get_rect(topleft = (100, 30))
        self.topleft = pygame.Vector2(self.rect.topleft)

        self.CELL_SIZE = self.surf.get_width() // 9

        self.cell_coords = []


        for i in range(1, 9):
        
            # horizontal line
            pygame.draw.line(self.surf, "black", (0, self.CELL_SIZE * i), (self.surf.get_width(), self.CELL_SIZE * i), 2)

            # vertical line
            pygame.draw.line(self.surf, "black", (self.CELL_SIZE * i, 0), (self.CELL_SIZE * i, self.surf.get_height()), 2)


    def coord_to_cell(self, coord: tuple | pygame.Vector2):

        if not isinstance(coord, pygame.Vector2):
            coord = pygame.Vector2(coord)

        return (coord - self.topleft) // self.CELL_SIZE

    def cell_to_coord(self, cell: tuple | pygame.Vector2):

        if not isinstance(cell, pygame.Vector2):
            cell = pygame.Vector2(cell)

        return self.topleft + pygame.Vector2(self.CELL_SIZE * cell.x, self.CELL_SIZE * cell.y)

    def draw(self, screen):
        screen.blit(self.surf, self.rect)
        pygame.draw.rect(screen, "black", self.rect, 3)


board = Board()

selected_surf = pygame.Surface((board.CELL_SIZE, board.CELL_SIZE))
selected_surf.fill("red")
selected_surf.set_alpha(50)


font = pygame.font.Font(size = 24)

mouse_pos = None

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


        if event.type == pygame.MOUSEMOTION:
            
            if board.rect.collidepoint(event.pos):
                mouse_pos = pygame.Vector2(event.pos)
                mouse_cell = board.coord_to_cell(mouse_pos)
            else:
                mouse_cell = None


    screen.fill("white")
    board.draw(screen)

    if mouse_cell is not None:
        screen.blit(selected_surf, board.cell_to_coord(mouse_cell))


    mouse_cell_text = font.render(f"{mouse_cell = }, {mouse_pos = }, {board.CELL_SIZE = }", True, "black")

    screen.blit(mouse_cell_text, (100, 10))


    pygame.display.flip()

    clock.tick(60)

pygame.quit()