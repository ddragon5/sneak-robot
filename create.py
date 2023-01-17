import pygame
import os
import random

import classes

snake_len = 3
width = 690  # 17 slots 53 pixel each
height = 600  # 15 slots 40 pixel each
background_colour = (10, 10, 10)


def create_backgound(screen):
    all_sprites_list = pygame.sprite.Group()
    Background_x = 0
    Background_y = 0
    os.chdir('png')
    Background_ = pygame.image.load('background.png')
    Background_ = pygame.transform.scale(Background_, (width, height))
    os.chdir(r'C:\Users\Lior\OneDrive\Documents\GitHub\sneak-robot')
    screen.blit(Background_, (Background_x, Background_y))
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
    g = int(width / 15)  # num of rows טורים
    f = int(height / 15)  # num of lines שורות
    size = (int(width / g), int(height / f))
    if (width / size[0]) % 2 == 0:
        f += 1
    h = (g * f)
    h = int(h)
    return size, g, f


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
        x_list = []
        for i in range(len(snakes)):
            x_list.append(snakes[i].x)
            x_list.append(snakes[i].y)
        if x1 in x_list:
            x1 = random.randint(1, g)  # get a random row to spawn in
            x = (x1 - 1) * size[0]  # get the x of the row
        if y1 in x_list:
            y1 = random.randint(1, f)  # get a random line to spawn in
            y = y1 * size[1]  # get the y of the line

        fruit = classes.fruit(x, y, size)
        fruits.append(fruit)
    return fruits
