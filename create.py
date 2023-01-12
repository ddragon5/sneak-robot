import pygame
import os


snake_len = 3
width = 690  # 17 slots 53 pixel each
height = 600  # 15 slots 40 pixel each
background_colour = (10, 10, 10)


def create_backgound(screen):
    all_sprites_list = pygame.sprite.Group()
    Background_x = int(width / 2)
    Background_y = int(height / 2)
    os.chdir('D:\python_projects\sneak robot\png')
    Background_ = pygame.image.load('background')
    return Background_


def window():
    pygame.display.set_caption('robot sneak')
    size = (width, height)
    screen = pygame.display.set_mode(size)
    screen.fill(background_colour)
    return screen


def size_squares(screen):
    slots_s = []
    slots_r = []
    snakes = []
    g = width / 15
    f = height / 15
    size = (width / g, height / f)
    if (width / size[0]) % 2 == 0:
        f += 1
    h = (g * f)
    h = int(h)
    return size


def snakes
