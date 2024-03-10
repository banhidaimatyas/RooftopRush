import pygame
from typing import Any


class Ground(pygame.sprite.Sprite):
    def __init__(self, ground_type: str, x: int, y: int):
        self.x_pos_ground: int = 0
        self.y_pos_ground: int = 800
        if ground_type == "1":
            self.image: pygame.Surface = pygame.image.load(
                "Img/Platform/1.png"
            ).convert_alpha()
        elif ground_type == "2":
            self.image: pygame.Surface = pygame.image.load(
                "Img/Platform/2.png"
            ).convert_alpha()
        elif ground_type == "3":
            self.image: pygame.Surface = pygame.image.load(
                "Img/Platform/3.png"
            ).convert_alpha()
        self.rect: pygame.Rect = pygame.Rect(x, y, 900, 600)

    def destroy(self):
        if self.rect.right <= -1:
            self.kill()

    def update(self, *args: Any, **kwargs: Any) -> None:
        super().update(*args, **kwargs)
        self.destroy()
