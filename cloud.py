import pygame
from typing import Any


class Cloud(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int):
        pygame.sprite.Sprite.__init__(self)
        

        self.image: pygame.Surface = pygame.image.load("Img/Map/cloud.png")
        self.rect: pygame.Rect = pygame.Rect(x, y, 321, 306)
        
        
    def update(self, *args: Any, **kwargs: Any) -> None:
        super().update(*args, **kwargs)
        