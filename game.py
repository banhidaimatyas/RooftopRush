import pygame

class Game:
    def __init__(self, width: int = 800, height: int = 600) -> None:
        pygame.init()
        
        self.width: int = width
        self.height: int = height
        
    def run(self) -> None:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()