import pygame

class Player:
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load('')
        self.rect = self.image.get_rect(topright = pos)
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 7
        self.gravity = 1
        self.jump_speed = -10
        self.on_ground = True

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        else:
            self.direction.x = 0
        
        if keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0

        if keys[pygame.K_SPACE] and self.on_ground:
            self.on_ground = False
            self.jump()

    def gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_speed

    def update(self):
        self.input()