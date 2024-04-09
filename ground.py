import pygame
from typing import Any
from settings import GAME_SPEED


class Ground(pygame.sprite.Sprite):
    def __init__(self, ground_type: str, x: int, y: int) -> None:
        pygame.sprite.Sprite.__init__(self)

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
        self.rect: pygame.Rect = pygame.Rect(x, y, 900, 450)

    def destroy(self) -> None:
        if self.rect.right <= -1:
            self.kill()

    def update(self, *args: Any, **kwargs: Any) -> None:
        super().update(*args, **kwargs)

        self.rect.x -= GAME_SPEED
        self.destroy()
