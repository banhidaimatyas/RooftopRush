from typing import Any
from settings import HEIGHT, WIDTH
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
        self.game_font = pygame.font.Font("Img/Font/tarrget.ttf", 30)
        self.font_colour = (255, 255, 255)

        self.menu()

    def bg(self) -> None:
        self.screen: pygame.Surface = pygame.display.set_mode((WIDTH, HEIGHT))
        self.bg_surf = pygame.image.load("Img/Map/background.jpg").convert_alpha()
        self.bg_surf = pygame.transform.scale(self.bg_surf, (900, 600)) # pygame.transform.rotozoom(self.bg_surf, 0, 1.5)
        self.bg_rect: pygame.rect.Rect = self.bg_surf.get_rect(topleft=(0, 0))

    def menu(self) -> None:
        self.screen: pygame.Surface = pygame.display.set_mode((WIDTH, HEIGHT))
        self.menu_surf = pygame.image.load("Img/Map/menu2.jpeg").convert_alpha()
        self.menu_surf = pygame.transform.scale(self.menu_surf, (900, 600))
        self.menu_rect: pygame.rect.Rect = self.bg_surf.get_rect(topleft=(0, 0))
        self.run_surf = self.game_font.render("Nyomd meg a SPACE-t az indításhoz!", True, self.font_colour)
        self.run_rect = self.run_surf.get_rect(center=(WIDTH / 2, HEIGHT / 2 - 60))


    

    def run(self) -> None:
        running: bool = True
        game_active: bool = False

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
                self.screen.blit(self.run_surf, self.run_rect)

                keys = pygame.key.get_pressed()
                if keys[pygame.K_SPACE]:
                    game_active = True

            
            
            

            pygame.display.update()
            self.clock.tick(60)
