from typing import Any
from support import import_folder
import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int):
        pygame.sprite.Sprite.__init__(self)
        self.animations = {'Idle': [], 'Running': []}
        # self.image = pygame.image.load(
        #     "Img/Character/PNG Sequences/Idle/0_Fallen_Angels_Idle_000.png"
        # ).convert_alpha()
        self.image = self.animations['idle'][self.frame_index]
        self.image = pygame.transform.rotozoom(self.image, 0, 0.1)
        self.frame_index = 0
        self.animation_speed = 0.15
        self.image = self.animations['idle'][self.frame_index]
        self.rect: pygame.Rect = self.image.get_rect(topright=(x, y))
        self.gravity_value: int = 1
        self.jump_speed: int = -10
        self.on_ground: bool = True
        self.gravity: int = 1
        self.jump_speed: int = -16
        self.dy: int = 0

        self.status = "Idle"


    def import_character_assets(self):
        character_path = "Img/Character/PNG Sequences"
        for animation in self.animation.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)

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
