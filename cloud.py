import pygame
from typing import Any


class Cloud(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int):
        pygame.sprite.Sprite.__init__(self)
        
        
        
    def update(self, *args: Any, **kwargs: Any) -> None:
        super().update(*args, **kwargs)
        