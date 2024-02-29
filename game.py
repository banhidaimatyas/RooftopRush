from typing import Any
from setting import HEIGHT, WIDTH
from player import Player

import pygame
import sys


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.clock = pygame.time.Clock()
        self.bg()
        
        self.characters: pygame.sprite.GroupSingle[Any] = pygame.sprite.GroupSingle()
        self.player: Player = Player(WIDTH // 2, HEIGHT // 2)

    def bg(self) -> None:
        self.screen: pygame.Surface = pygame.display.set_mode((WIDTH, HEIGHT))
        self.bg_surf = pygame.image.load("Img/Map/background.jpg").convert_alpha()
        self.bg_surf = pygame.transform.scale(self.bg_surf, (900, 600)) # pygame.transform.rotozoom(self.bg_surf, 0, 1.5)
        self.bg_rect: pygame.rect.Rect = self.bg_surf.get_rect(topleft=(0, 0))

    def run(self) -> None:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit
            self.characters.add(self.player)
            self.screen.blit(self.bg_surf, self.bg_rect)
            self.characters.draw(self.screen)
            self.player.update()
            
            
            

            pygame.display.update()
            self.clock.tick(60)
