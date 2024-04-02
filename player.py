from typing import Any
from support import import_folder
from settings import CH_POS_Y, CH_SPEED, WIDTH
import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int):
        pygame.sprite.Sprite.__init__(self)
        self.animations: dict[str, list[pygame.Surface]] = {
            "Running": [],
            "Jumping": [],
            "Sliding": [],
        }
        self.double_jump_activated: bool = False
        self.sliding: bool = False
        self.frame_index: float = 0
        self.animation_speed: float = CH_SPEED
        self.setting_gravity()
        self.import_character_assets()
        self.get_status()
        self.animate()

        self.ch_height: int = 63
        self.ch_width: int = 45
        self.image: pygame.Surface = self.animations[self.status][0]
        self.rect = pygame.Rect(x, y, self.ch_width, self.ch_height)

        self.x_pos: int = x
        self.y_pos: int = y
        self.reset()

    def reset(self):
        self.x_pos = self.x_pos
        self.y_pos = self.y_pos
        self.rect: pygame.Rect = pygame.Rect(self.x_pos, self.y_pos, 45, 63)

    def setting_gravity(self):
        self.on_ground: bool = True
        self.gravity: int = 1
        self.jump_speed: int = -16
        self.dy: int = 0
        self.jumping: int = 0  # jumping status

    def animate(self):
        animation: list[pygame.Surface] = self.animations[self.status]
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index: float = 0
        self.image: pygame.Surface = animation[int(self.frame_index)]

    def get_status(self):
        if self.on_ground:
            if self.sliding:
                self.status: str = "Sliding"
            else:
                self.status: str = "Running"
        else:
            self.status: str = "Jumping"

    def import_character_assets(self):
        character_path = "Img/Character/PNG Sequences/"
        for animation in self.animations.keys():
            full_path: str = character_path + animation
            self.animations[animation] = import_folder(full_path)

    def input(self):
        keys: pygame.key.ScancodeWrapper = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.on_ground and not keys[pygame.K_DOWN]:
            self.jump()

        elif (
            keys[pygame.K_UP]
            and self.double_jump_activated
            and not self.on_ground
            and self.jumping == 1
            and self.dy >= -5
            and not keys[pygame.K_DOWN]
        ):
            self.second_jump()

        if keys[pygame.K_DOWN] and self.on_ground:
            self.sliding: bool = True
            self.slide()
        else:
            self.sliding: bool = False
        if not keys[pygame.K_UP] and not keys[pygame.K_DOWN] and self.on_ground:
            self.run()
        if keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
            self.horizontal_movement(-3)
            self.changing_speed(False, True)
        if keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]:
            self.horizontal_movement(2)
            self.changing_speed(True, False)
        if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
            self.changing_speed(False, False)

    def changing_speed(self, getting_faster: bool, slowing_down: bool):
        

    def horizontal_movement(self, x: int):
        self.rect.x += x
        if self.rect.x > WIDTH - 200 or self.rect.x < 200:
            self.rect.x -= x

    def apply_gravity(self):
        self.dy += self.gravity
        self.rect.y += self.dy

    def jump(self):
        self.dy: int = self.jump_speed
        self.on_ground: bool = False
        self.sliding: bool = False
        self.jumping: int = 1

    def second_jump(self):
        self.dy: int = -15
        self.jumping: int = 2

    def slide(self):
        self.rect.height = 47
        self.rect.top = self.y_pos + 16

    def run(self):
        self.rect.height = self.ch_height
        self.rect.top = CH_POS_Y

    def update(self, *args: Any, **kwargs: Any) -> None:
        super().update(*args, **kwargs)
        self.input()
        self.get_status()
        self.animate()
        self.apply_gravity()
