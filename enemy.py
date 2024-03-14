import pygame
from typing import Any
from settings import GAME_SPEED

class Enemy(pygame.sprite.Sprite):
    def __init__(self, enemy_type: str, x: int, y: int):
        pygame.sprite.Sprite.__init__(self)

        if enemy_type == "1":
            self.image: pygame.Surface = pygame.image.load(
                "Img/Enemy/bat1.png"
            ).convert_alpha()
            self.image = pygame.transform.rotozoom(self.image, 0, 0.2)
            self.rect: pygame.Rect = pygame.Rect(x, y, 393, 154)
        elif enemy_type == "2":
            self.image: pygame.Surface = pygame.image.load(
                "Img/Enemy/szörny1.png"
            ).convert_alpha()
            self.image = pygame.transform.rotozoom(self.image, 0, 1)
            self.rect: pygame.Rect = pygame.Rect(x, y, 54, 71)
        
        

        


    def destroy(self):
        if self.rect.right <= -1:
            self.kill()

    def update(self, *args: Any, **kwargs: Any) -> None:
        super().update(*args, **kwargs)

        self.rect.x -= GAME_SPEED
        self.destroy()