import pygame


class Player:
    def __init__(self, pos: tuple[int]):
        super().__init__()
        self.image = pygame.image.load("")
        self.rect: pygame.Rect = self.image.get_rect(topright=pos)
        self.direction = pygame.math.Vector2(0, 0)
        self.speed: int = 7
        self.gravity_value: int = 1
        self.jump_speed: int = -10
        self.on_ground: bool = True

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.on_ground:
            self.on_ground = False
            self.jump()
        if keys[pygame.K_DOWN] and self.on_ground:
            self.slide()

    def slide(self):
        pass
        
    def gravity(self):
        self.direction.y += self.gravity_value
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_speed

    def update(self):
        self.input()
