import pygame
import os

import classes

snake_len = 3
width = 690  # 17 slots 53 pixel each
height = 600  # 15 slots 40 pixel each
background_colour = (10, 10, 10)


def create_backgound(screen):
    all_sprites_list = pygame.sprite.Group()
    Background_x = int(width / 2)
    Background_y = int(height / 2)
    Background_ = pygame.image.load('background')
    Background_ = pygame.transform.scale(Background_, (width, height))
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
    return size, g, f


def create_snakes():
    snakes = []
    for i in range(snake_len):
        snake = classes.snake
        snakes.append(snake)
    return snakes