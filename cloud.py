import pygame
from typing import Any


class Cloud(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int) -> None:
        pygame.sprite.Sprite.__init__(self)

        self.rect: pygame.Rect = pygame.Rect(x, y, 321, 306)
        self.image: pygame.Surface = pygame.image.load(
            "Img/Map/cloud.png"
        ).convert_alpha()
        self.image: pygame.Surface = pygame.transform.rotozoom(self.image, 0, 0.2)

    def moving_left(self) -> None:
        self.rect.x += -5

    def destroy(self) -> None:
        if self.rect.x < -400:
            self.kill()

    def update(self, *args: Any, **kwargs: Any) -> None:
        super().update(*args, **kwargs)
        self.moving_left()
        self.destroy()
