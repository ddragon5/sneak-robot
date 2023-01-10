import pygame
import torch

import classes

snake_len = 3
width = 690  # 17 slots 53 pixel each
height = 600  # 15 slots 40 pixel each
background_colour = (151, 251, 252)


def create_backgound(screen):
    all_sprites_list = pygame.sprite.Group()
    Background_x = 0
    Background_y = 0
    Background_ = pygame.Rect(Background_x, Background_y, width, height)
    pygame.draw.rect(screen, background_colour, Background_)
    return Background_


def window():
    pygame.display.set_caption('robot sneak')
    size = (width, height)
    screen = pygame.display.set_mode(size)
    screen.fill(background_colour)
    return screen


def floor(screen):
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
    for i in range(h):
        slot = classes.tails(size, slots_s, screen)
        slot.index = i
        slots_s.append(slot)
        slots_r.append(slot.rect)
        if 'snake' in slot.tag:  # create a group of only the snake
            slot.color = (138, 43, 226)
            snakes.append(slot)
    return slots_s, slots_r, snakes
