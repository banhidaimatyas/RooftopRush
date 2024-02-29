from typing import Any
from support import import_folder
from setting import CH_SPEED
import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int):
        pygame.sprite.Sprite.__init__(self)
        self.animations: dict[str, list[pygame.Surface]] = {"Running": []}
        # self.image = pygame.image.load(
        #     "Img/Character/PNG Sequences/Idle/0_Fallen_Angels_Idle_000.png"
        # ).convert_alpha()
        self.frame_index = 0
        self.import_character_assets()
        self.animation_speed: float = CH_SPEED
        self.status = "Running"
        self.animate()
        self.image = self.animations["Running"][4]

        self.rect: pygame.Rect = self.image.get_rect(topright=(x, y))

        self.setting_gravity()

    def setting_gravity(self):
        self.gravity_value: int = 1
        self.jump_speed: int = -10
        self.on_ground: bool = True
        self.gravity: int = 1
        self.jump_speed: int = -16
        self.dy: int = 0

    def animate(self):
        animation = self.animations[self.status]
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0
        self.image = animation[int(self.frame_index)]

    def get_status(self):
        self.status = "Running"

    def import_character_assets(self):
        character_path = "Img/Character/PNG Sequences/"
        for animation in self.animations.keys():
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
        self.input()
        self.get_status()
        self.animate()
        self.apply_gravity()
