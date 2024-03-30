from typing import Any
from settings import CH_POS_X, CH_POS_Y, GAME_SPEED, HEIGHT, WIDTH
from player import Player
import random
from ground import Ground
from enemy import Enemy

import pygame
import sys


class Game:

    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption("Rooftop Rush")
        self.clock = pygame.time.Clock()
        self.bg()

        self.characters: pygame.sprite.GroupSingle[Any] = pygame.sprite.GroupSingle()
        self.player: Player = Player(CH_POS_X, CH_POS_Y)
        self.game_font = pygame.font.Font("Img/Font/tarrget.ttf", 30)
        self.score_font = pygame.font.SysFont("Arial", 30)
        self.font_colour = (255, 255, 255)

        self.menu()
        
        # self.score()

        self.win = False

        self.obstacles: pygame.sprite.Group[Any] = pygame.sprite.Group()

        global x_pos_ground, y_pos_ground, points, highest

        self.enemies: pygame.sprite.Group[Any] = pygame.sprite.Group()

        x_pos_ground = 0
        y_pos_ground = 450
        image_width = 900
        points = 0
        highest = 0
        self.obstacles.add(Ground(self.ground_choosing(), x_pos_ground, y_pos_ground))
        self.obstacles.add(
            Ground(
                self.ground_choosing(),
                image_width + x_pos_ground,
                y_pos_ground,
            )
        )
        self.end_screen()

       
        self.enemy_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.enemy_timer, 1500)
        



    def bg(self) -> None:
        self.screen: pygame.Surface = pygame.display.set_mode((WIDTH, HEIGHT))
        self.bg_surf = pygame.image.load("Img/Map/background.jpg").convert_alpha()
        self.bg_surf = pygame.transform.scale(
            self.bg_surf, (900, 600)
        )  # pygame.transform.rotozoom(self.bg_surf, 0, 1.5)
        self.bg_rect: pygame.rect.Rect = self.bg_surf.get_rect(topleft=(0, 0))

    def menu(self) -> None:
        self.screen: pygame.Surface = pygame.display.set_mode((WIDTH, HEIGHT))
        self.menu_surf = pygame.image.load("Img/Map/menu2.jpeg").convert_alpha()
        self.menu_surf = pygame.transform.scale(self.menu_surf, (900, 600))
        self.menu_rect: pygame.rect.Rect = self.bg_surf.get_rect(topleft=(0, 0))
        self.run_surf = self.game_font.render(
            "Nyomd meg a [SPACE]-t az indításhoz!", True, self.font_colour
        )
        self.run_rect = self.run_surf.get_rect(center=(WIDTH / 2, HEIGHT / 2 - 60))

    def end_screen(self) -> None:
        self.game_end: bool = False
        global highest, points
        # points = 0
        # highscore: int = highest
        self.screen: pygame.Surface = pygame.display.set_mode((WIDTH, HEIGHT))
        self.end_surf = pygame.image.load("Img/Map/end_screen.jpg").convert_alpha()
        self.end_surf = pygame.transform.scale(self.end_surf, (900, 600))
        self.end_rect: pygame.rect.Rect = self.end_surf.get_rect(topleft=(0, 0))
        self.end_text_surf = self.game_font.render("Nyomd meg az [R]-t az újraindításhoz!", True, self.font_colour)
        self.end_text_rect = self.end_text_surf.get_rect(center=(WIDTH / 2, HEIGHT / 2 - 60))
        # self.h_points_surf = self.game_font.render(f"Legmagasabb pontszám: {highest}", True, self.font_colour)
        # self.h_points_rect = self.h_points_surf.get_rect(center=(WIDTH / 2, HEIGHT / 2 - 30))

    def update_hiscore(self) -> None:
        self.h_points_surf = self.game_font.render(f"Legmagasabb pontszám: {highest}", True, self.font_colour)
        self.h_points_rect = self.h_points_surf.get_rect(center=(WIDTH / 2, HEIGHT / 2 - 30))

    def score(self) -> None:
        global points
        self.game_speed = GAME_SPEED
        points += 1
        if points % 1000 == 0:
            self.game_speed += 0.5

        # if self.game_end:
            

        self.score_surf = self.score_font.render(
            "Pontszám: " + str(points), True, (255, 255, 255)
        )
        self.score_rect = self.score_surf.get_rect(topleft=(0, 0))
        self.screen.blit(self.score_surf, self.score_rect)

    def ground_choosing(self) -> str:
        ground_list: list[str] = ["1", "2", "3"]
        return random.choice(ground_list)

    def ground_generating(self):
        global x_pos_ground, y_pos_ground
        image_width: int = 900
        if x_pos_ground <= 0:
            self.obstacles.add(
                Ground(
                    self.ground_choosing(),
                    image_width + x_pos_ground,
                    y_pos_ground,
                )
            )
            x_pos_ground = 900
        x_pos_ground -= GAME_SPEED

    def y_movement_collision(self) -> None:
        if pygame.sprite.spritecollide(self.player, self.obstacles, False):
            self.player.on_ground = True
            self.player.dy = -1

    def x_movement_collision(self) -> None:
        if (
            self.player.rect.x >= x_pos_ground - 900
            and self.player.rect.y >= y_pos_ground
            and pygame.sprite.spritecollide(self.player, self.obstacles, False)
        ):
            self.player.reset()

    
    def enemy_check(self) -> None:
        if pygame.sprite.spritecollide(self.player, self.enemies, False):
            self.game_end = True


    def run(self) -> None:
        running: bool = True
        self.game_active: bool = False
        
        global points, highest

        if running is False:
            pygame.quit()
            sys.exit()
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == self.enemy_timer and self.game_active:
                    enemy_type: str = random.choice(["1","2"])
                    self.ground_choosing()
                    if enemy_type == "1":
                        self.enemies.add(Enemy(enemy_type, random.randint(900, 900), 380))
                    else:                
                        self.enemies.add(Enemy(enemy_type, random.randint(900, 900), 380))


            if self.game_active is True:


                self.screen.blit(self.bg_surf, self.bg_rect)

                self.characters.add(self.player)
                self.characters.draw(self.screen)
                self.player.update()

                self.ground_generating()
                self.obstacles.draw(self.screen)
                self.obstacles.update()
                self.enemies.draw(self.screen)
                self.enemies.update()
                self.y_movement_collision()

                self.x_movement_collision()

                self.enemy_check()

                self.score()


            elif not self.win:

                self.screen.blit(self.menu_surf, self.menu_rect)
                self.screen.blit(self.run_surf, self.run_rect)

                keys = pygame.key.get_pressed()
                if keys[pygame.K_SPACE]:
                    self.game_active = True

            if self.game_end:
                # self.end_screen()
                self.update_hiscore()
                self.win = True
                self.game_active = False
                self.screen.blit(self.end_surf, self.end_rect)
                self.screen.blit(self.end_text_surf, self.end_text_rect)
                keys = pygame.key.get_pressed()
                if points >= highest:
                    highest = points
                self.screen.blit(self.h_points_surf, self.h_points_rect)
                if keys[pygame.K_r]:
                    self.game_active = True
                    points = 0

            pygame.display.update()
            self.clock.tick(60)
