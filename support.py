from os import walk
import pygame


def import_folder(path: str) -> list[pygame.Surface]:
    surface_list: list[pygame.Surface] = []

    for _, __, img_files in walk(path):
        for image in img_files:
            full_path: str = path + "/" + image
            image_surf = pygame.image.load(full_path).convert_alpha()
            image_surf = pygame.transform.rotozoom(image_surf, 0, 0.1)
            surface_list.append(image_surf)
    return surface_list
