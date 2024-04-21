import pygame
from typing import Any


class Enemy(pygame.sprite.Sprite):
    def __init__(self, enemy_type: str, x: int, y: int, difficulty_number: int) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.enemy_type: str = enemy_type
        self.counter: int = 0
        self.surf_index = 0
        difficulties: list[int] = [10, 11, 12, 13, 14, 15, 16, 17, 20, 22, 25, 27]
        self.actual_difficulty: int = difficulties[difficulty_number]
        if enemy_type == "1":
            self.surfaces: list[pygame.Surface] = [
                pygame.image.load("Img/Enemy/bat_1.png").convert_alpha(),
                pygame.image.load("Img/Enemy/bat_2.png").convert_alpha(),
            ]
            self.image: pygame.Surface = self.surfaces[0]
            self.rect: pygame.Rect = pygame.Rect(x, y, 70, 25)
        elif enemy_type == "2":
            self.surfaces: list[pygame.Surface] = [
                pygame.image.load("Img/Enemy/monster_1.png").convert_alpha(),
                pygame.image.load("Img/Enemy/monster_2.png").convert_alpha(),
            ]
            self.image: pygame.Surface = self.surfaces[0]
            self.rect: pygame.Rect = pygame.Rect(x, y, 54, 71)

    def changing_images(self) -> None:
        self.counter += 1
        if self.counter % 7 == 0:
            self.surf_index += 1
        if self.surf_index > len(self.surfaces) - 1:
            self.surf_index: int = 0
        self.image = self.surfaces[self.surf_index]

    def shrinking_bat_images(self) -> None:
        if self.enemy_type == "1":
            self.image = pygame.transform.rotozoom(self.image, 0, 0.15)

    def destroy(self) -> None:
        if self.rect.right <= -1:
            self.kill()

    def update(self, *args: Any, **kwargs: Any) -> None:
        super().update(*args, **kwargs)
        self.changing_images()
        self.shrinking_bat_images()
        self.rect.x -= self.actual_difficulty
        self.destroy()
