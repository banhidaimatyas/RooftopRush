from setting import HEIGHT, WIDTH

import pygame
import sys


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.clock = pygame.time.Clock()
        self.bg()

    def bg(self) -> None:
        self.screen: pygame.Surface = pygame.display.set_mode((WIDTH, HEIGHT))
        self.bg_surf = pygame.image.load(
            "Img/Map/background.png"
        ).convert_alpha()
        self.bg_surf = pygame.transform.rotozoom(self.bg_surf, 0, 1.5)
        self.bg_rect: pygame.rect.Rect = self.bg_surf.get_rect(topleft=(0, 0))

    def run(self) -> None:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit
            
            self.screen.blit(self.bg_surf, self.bg_rect)
            pygame.display.update()
            self.clock.tick(60)
