import pygame
import os
import random

import classes

snake_len = 3
width = 690
height = 600
background_colour = (135, 206, 235)


def create_backgound(screen):
    all_sprites_list = pygame.sprite.Group()
    Background_x = 0
    Background_y = 0
    path = os.getcwd()
    os.chdir('png')
    Background_ = pygame.image.load('background.png')
    Background_ = pygame.transform.scale(Background_, (width, height))
    os.chdir(path)
    screen.blit(Background_, (Background_x, Background_y))
    return Background_

########################################################################################################################

def window():
    pygame.display.set_caption('robot sneak')
    size = (width, height)
    screen = pygame.display.set_mode(size)
    screen.fill(background_colour)
    return screen

########################################################################################################################

def size_squares(screen):
    slots_s = []
    slots_r = []
    snakes = []
    g = int(width / 15)  # num of rows טורים
    f = int(height / 15)  # num of lines שורות
    size = (int(width / g), int(height / f))
    if (width / size[0]) % 2 == 0:
        f += 1
    h = (g * f)
    h = int(h)
    return size, g, f

########################################################################################################################

def create_snakes(size, g, f):
    snakes = []
    for i in range(snake_len):
        snake = classes.snake(snakes, size, g, f)
        snakes.append(snake)
    return snakes

########################################################################################################################


def create_fruit(size, g, f, snakes):
    fruits = []
    for i in range(2):  # spawn 2 fruits
        x1 = random.randint(1, g)  # get a random row to spawn in
        x = (x1 - 1) * size[0]  # get the x of the row
        y1 = random.randint(1, f)  # get a random line to spawn in
        y = y1 * size[1]  # get the y of the line
        for n in range(len(snakes)):
            snake_pos = (snakes[n].x, snakes[n].y)
            fruit_pos = (x, y)
            if fruit_pos == snake_pos:
                x1 = random.randint(1, g)  # get a random row to spawn in
                x = (x1 - 1) * size[0]  # get the x of the row
                y1 = random.randint(1, f)  # get a random line to spawn in
                y = y1 * size[1]  # get the y of the line
                fruit_pos = (x, y)

        fruit = classes.fruit(x, y, size)
        fruits.append(fruit)
    return fruits
