from typing import Any
from setting import HEIGHT, WIDTH
from player import Player

import pygame
import sys


class Game:
    

    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption("Rooftop Rush")
        self.clock = pygame.time.Clock()
        self.bg()
        
        self.characters: pygame.sprite.GroupSingle[Any] = pygame.sprite.GroupSingle()
        self.player: Player = Player(WIDTH // 2, HEIGHT // 2)

    def bg(self) -> None:
        self.screen: pygame.Surface = pygame.display.set_mode((WIDTH, HEIGHT))
        self.bg_surf = pygame.image.load("Img/Map/background.jpg").convert_alpha()
        self.bg_surf = pygame.transform.scale(self.bg_surf, (900, 600)) # pygame.transform.rotozoom(self.bg_surf, 0, 1.5)
        self.bg_rect: pygame.rect.Rect = self.bg_surf.get_rect(topleft=(0, 0))

    def menu(self) -> None:
        self.screen: pygame.Surface = pygame.display.set_mode((WIDTH, HEIGHT))
        self.menu_surf = pygame.image.load("Img/Map/menu.jpg").convert_alpha()
        self.menu_surf = pygame.transform.scale(self.menu_surf, (900, 600))
        self.menu_rect: pygame.rect.Rect = self.bg_surf.get_rect(topleft=(0, 0))
        self.game_font = pygame.font.SysFont('arial', 200, bold = True)
        self.run_surf = self.game_font.render("Nyomd meg a SPACE-t az indításhoz!", True, 255,255,255)
        self.run_rect = self.run_surf.get


    

    def run(self) -> None:
        running: bool = True
        game_active: bool = True

        if running is False:
            pygame.quit()
            sys.exit
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            if game_active is True:
                self.characters.add(self.player)
                self.screen.blit(self.bg_surf, self.bg_rect)
                self.characters.draw(self.screen)
                self.player.update()
            
            else:
                self.screen.blit(self.menu_surf, self.menu_rect)

            
            
            

            pygame.display.update()
            self.clock.tick(60)
