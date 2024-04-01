import pygame
from typing import Any
from settings import GAME_SPEED


class Enemy(pygame.sprite.Sprite):
    def __init__(self, enemy_type: str, x: int, y: int):
        pygame.sprite.Sprite.__init__(self)
        self.enemy_type: str = enemy_type
        list_of_surfaces: list[pygame.Surface] = []
        self.counter: int = 0

        if enemy_type == "1":
            list_of_surfaces = [
                pygame.image.load("Img/Enemy/bat1.png").convert_alpha(),
                pygame.image.load("Img/Enemy/bat2.png").convert_alpha(),
            ]
            self.image = self.animation(list_of_surfaces)
            self.image = pygame.transform.rotozoom(self.image, 0, 0.15)
            self.rect: pygame.Rect = pygame.Rect(x, y, 70, 25)
        elif enemy_type == "2":
            list_of_surfaces = [
                pygame.image.load("Img/Enemy/szörny1.png").convert_alpha(),
                pygame.image.load("Img/Enemy/szörny2.png").convert_alpha(),
            ]
            self.image = self.animation(list_of_surfaces)
            self.image = pygame.transform.rotozoom(self.image, 0, 1)
            self.rect: pygame.Rect = pygame.Rect(x, y, 54, 71)

    def animation(self, list_of_surfaces: list[pygame.Surface]) -> pygame.Surface:
        surf_index = 0
        
        if self.counter % 7:
            surf_index += 1
        if surf_index > len(list_of_surfaces) - 1:
            surf_index = 0
            
        image: pygame.Surface = list_of_surfaces[surf_index]
        return image

    def destroy(self):
        if self.rect.right <= -1:
            self.kill()

    def update(self, *args: Any, **kwargs: Any) -> None:
        super().update(*args, **kwargs)
        self.counter += 1
        self.rect.x -= GAME_SPEED
        self.destroy()
