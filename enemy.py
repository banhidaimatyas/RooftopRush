import pygame
from typing import Any
from settings import GAME_SPEED


class Enemy(pygame.sprite.Sprite):
    def __init__(self, enemy_type: str, x: int, y: int):
        pygame.sprite.Sprite.__init__(self)
        self.enemy_type: str = enemy_type
        self.counter: int = 0
        self.surf_index = 0
        if enemy_type == "1":
            self.surfaces: list[pygame.Surface] = [
                pygame.image.load("Img/Enemy/bat1.png").convert_alpha(),
                pygame.image.load("Img/Enemy/bat2.png").convert_alpha(),
            ]
            self.image = self.surfaces[0]
            self.rect: pygame.Rect = pygame.Rect(x, y, 70, 25)
        elif enemy_type == "2":
            self.surfaces: list[pygame.Surface] = [
                pygame.image.load("Img/Enemy/szörny1.png").convert_alpha(),
                pygame.image.load("Img/Enemy/szörny2.png").convert_alpha(),
            ]
            self.image = self.surfaces[0]
            self.rect: pygame.Rect = pygame.Rect(x, y, 54, 71)

    def changing_images(self):
        self.counter += 1
        if self.counter % 7 == 0:
            self.surf_index += 1
        if self.surf_index > len(self.surfaces) - 1:
            self.surf_index = 0
        self.image = self.surfaces[self.surf_index]

    def shrinking_bat_images(self):
        if self.enemy_type == '1':
            self.image = pygame.transform.rotozoom(self.image, 0, 0.15)
    
    def destroy(self):
        if self.rect.right <= -1:
            self.kill()

    def update(self, *args: Any, **kwargs: Any) -> None:
        super().update(*args, **kwargs)
        self.changing_images()
        self.shrinking_bat_images()
        self.rect.x -= GAME_SPEED+2
        self.destroy()
