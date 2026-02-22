import pygame
import configs
from board import Board


class Game: 
    
    def __init__(self):
       pygame.init()
       self.screen = pygame.display.set_mode(configs.SCREEN_SIZE)
       pygame.display.set_caption("Sudoku")
       self.running = True
       self.board = Board()
    
    def events(self):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
       
    def run(self):
        while self.running:
            pygame.display.flip()
            self.events()
            self.screen.fill(configs.BG_COLOR)
            self.board.draw(self.screen)

if __name__ == "__main__":
    game = Game()
    game.run()