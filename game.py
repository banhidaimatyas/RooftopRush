import pygame

class Game:
    def __init__(self) -> None:
        pygame.init()
        
    def run(self) -> None:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()