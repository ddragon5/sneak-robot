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


########################################################################################################################


def create_buttons(pos):
    buttons = []
    path = os.getcwd()
    os.chdir('png')
    start_image = pygame.image.load('start.png')
    start_image = pygame.transform.scale(start_image, (400, 500))
    y = pos[1]
    y = y + 50
    x = (width - start_image.get_size()[0]) / 2
    pos = (x, y)
    START_BUTTON = classes.Button(start_image, pos, start_image, (0, 183, 239))
    buttons.append(START_BUTTON)

    settings_image = pygame.image.load('settings.png')
    settings_image = pygame.transform.scale(settings_image, (400, 500))
    y = pos[1]
    y += 80
    pos = (x, y)
    SETTINGS_BUTTON = classes.Button(settings_image, pos, settings_image, (0, 183, 239))
    buttons.append(SETTINGS_BUTTON)

    Quit_image = pygame.image.load('quit.png')
    Quit_image = pygame.transform.scale(Quit_image, (400, 500))
    y = pos[1]
    y += 80
    pos = (x, y)
    QUIT_BUTTON = classes.Button(Quit_image, pos, Quit_image, (0, 183, 239))
    buttons.append(QUIT_BUTTON)

    os.chdir(path)
    return START_BUTTON, SETTINGS_BUTTON, QUIT_BUTTON, buttons


########################################################################################################################


def create_settings(pos):
    buttons = []
    path = os.getcwd()
    os.chdir('png')
    colorkey = (0, 183, 239)
    from classes import Button

    difficulty_image = pygame.image.load('difficulty.png')
    difficulty_image = pygame.transform.scale(difficulty_image, (400, 500))
    y = pos[1]
    y = 30
    x = (width - difficulty_image.get_size()[0]) / 3
    pos = (x, 30)
    DIFFICULTY_BUTTON = Button(difficulty_image, pos, difficulty_image, colorkey)
    # SLIDER
    y = pos[1]
    y = 30
    x += 20
    pos = (x, 30)
    difficulty_slider = []
    for i in range(1, 4):
        print((str(i) + '.png'))
        difficulty_image = pygame.image.load((str(i) + '.png'))
        difficulty_image = pygame.transform.scale(difficulty_image, (400, 500))

        DIFFICULTY_SLIDER = Button(difficulty_image, pos, difficulty_image, colorkey)
        difficulty_slider.append(DIFFICULTY_SLIDER)

    size_image = pygame.image.load('size.png')
    size_image = pygame.transform.scale(size_image, (400, 500))
    y = pos[1]
    y = y + 80
    x -= 20
    pos = (x, y)
    SIZE_BUTTON = Button(size_image, pos, size_image, colorkey)

    os.chdir(path)
    return DIFFICULTY_BUTTON, SIZE_BUTTON, difficulty_slider #, SKINS

