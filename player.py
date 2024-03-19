from typing import Any
from support import import_folder
from settings import CH_POS_Y, CH_SPEED
import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int):
        pygame.sprite.Sprite.__init__(self)
        self.animations: dict[str, list[pygame.Surface]] = {
            "Running": [],
            "Jumping": [],
            "Sliding": [],
        }
        # self.image = pygame.image.load(
        #     "Img/Character/PNG Sequences/Idle/0_Fallen_Angels_Idle_000.png"
        # ).convert_alpha()

        self.ch_height: int = 63
        self.ch_width: int = 45

        self.setting_gravity()
        self.sliding: bool = False
        self.frame_index = 0
        self.import_character_assets()
        self.animation_speed: float = CH_SPEED
        self.get_status()
        self.animate()
        self.image = self.animations[self.status][0]

        # self.rect: pygame.Rect = self.image.get_rect(topright=(x, y))
        self.rect = pygame.Rect(x, y, self.ch_width, self.ch_height)

        self.x_pos: int = x
        self.y_pos: int = y
        self.reset()

    def reset(self):
        self.x_pos = self.x_pos
        self.y_pos = self.y_pos
        self.rect = pygame.Rect(self.x_pos, self.y_pos, 45, 63)

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
        if self.on_ground:
            if self.sliding:
                self.status = "Sliding"
            else:
                self.status = "Running"
        else:
            self.status = "Jumping"

    def import_character_assets(self):
        character_path = "Img/Character/PNG Sequences/"
        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.on_ground:
            self.on_ground = False
            self.sliding = False
            self.jump()
        if keys[pygame.K_DOWN] and self.on_ground:
            self.sliding = True
            self.slide()
        else:
            self.sliding = False
        if not keys[pygame.K_UP] and keys[pygame.K_DOWN]:
            self.run()

    def apply_gravity(self):
        self.dy += self.gravity
        self.rect.y += self.dy

    def jump(self):
        self.dy = self.jump_speed

    def slide(self):
        self.rect.height = self.ch_height // 2

    def run(self):
        self.rect.height = self.ch_height
        self.rect.top = CH_POS_Y

    def update(self, *args: Any, **kwargs: Any) -> None:
        super().update(*args, **kwargs)
        self.input()
        self.get_status()
        self.animate()
        self.apply_gravity()
