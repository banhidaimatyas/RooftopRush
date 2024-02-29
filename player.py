from typing import Any
import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(
            "Img/Character/PNG Sequences/Idle/0_Fallen_Angels_Idle_000.png"
        ).convert_alpha()
        self.image = pygame.transform.rotozoom(self.image, 0, 0.1)
        self.rect: pygame.Rect = self.image.get_rect(topright=(x, y))
        self.gravity_value: int = 1
        self.jump_speed: int = -10
        self.on_ground: bool = True
        self.gravity: int = 1
        self.jump_speed: int = -16
        self.dy: int = 0

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.on_ground:
            self.on_ground = False
            self.jump()

    def apply_gravity(self):
        self.dy += self.gravity
        self.rect.y += self.dy

    def jump(self):
        self.on_ground: bool = False
        self.dy = self.jump_speed

    def update(self, *args: Any, **kwargs: Any) -> None:
        super().update(*args, **kwargs)
        self.apply_gravity()
        self.input()
