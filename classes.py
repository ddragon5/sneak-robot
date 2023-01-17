import pygame
from enum import Enum
import random

import misc


class Spots(Enum):
    BLANK = 0
    TAIL = 1
    BODY = 2
    HEAD = 3
    FRUIT = 4


class Dir(Enum):
    UP = 1
    DOWN = 2
    RIGHT = 3
    LEFT = 4


class snake(pygame.sprite.Sprite):
    def __init__(self, snakes, size, g, f):
        super(pygame.sprite.Sprite, self).__init__()
        self.color = (236, 231, 2)  # color of the snake
        # find place on the grid
        line = f // 2  # קו ישר
        row = 11  # טור
        for i in range(len(snakes)):
            row += 1
        self.type = Spots.BLANK
        if row == 11:
            self.type = Spots.TAIL
            self.color = (78, 211, 0)
        if row == 13:
            self.type = Spots.HEAD
            self.color = (228, 145, 0)
        if row == 12:
            self.type = Spots.BODY
        self.gir_pos = (line, row)
        # find x and y
        self.x = (row - 1) * size[0]
        self.y = line * size[1]
        self.size = size
        self.dir = Dir.RIGHT
        self.index = len(snakes)
        self.rect = pygame.Rect(self.x, self.y, size[0], size[1])
        self.image = pygame.Surface(size)
        self.image.fill(self.color)
        self.s_dir = self.dir
        self.id = "pos: ", self.gir_pos, "x and y: ", self.x, self.y, self.dir, 'index: ', self.index, self.rect, self.type

    def update(self, screen, snakes):
        size = self.size
        t = self.x
        if self.dir == Dir.RIGHT:
            self.x += 15
        if self.dir == Dir.LEFT:
            self.x -= 15
        if self.dir == Dir.UP:
            self.y += 15
        if self.dir == Dir.DOWN:
            self.y -= 15
        self.x = int(self.x)
        self.y = int(self.y)
        self.rect.update(self.x, self.y, size[0], size[1])
        screen.blit(self.image, (self.x, self.y))
        try:
            self.dir = snakes[self.index+1].dir
        except IndexError:
            pass
        snakes[self.index] = self
        return snakes

    def check(self, snakes, Background_, fruits, screen, g):
        Background_rect = Background_.get_rect()
        is_dead = False
        a = False
        b = False
        # checking if out of bonds
        if Background_rect.contains(self.rect) == False:
            is_dead = True
            a = True
        # checking if he collided with him self except if he hit his neck
        for i in range(len(snakes) - 2):
            s = snakes[i]
            r = s.rect
            is_dead = self.rect.colliderect(r)  # True or False
            b = True
        # checking if the snakes has eaten a fruit
        for i in range(len(fruits)):
            t = fruits[i]
            if self.rect.contains(t.rect):
                t = t.spawn(screen, snakes, g)
                fruits[i] = t
                snakes = misc.longer(snakes, self.size, g)
        return is_dead, fruits, snakes

########################################################################################################################
class fruit(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        super(pygame.sprite.Sprite, self).__init__()
        self.type = Spots.FRUIT
        self.x = x
        self.y = y
        self.color = (243, 11, 28)
        self.rect = pygame.Rect(self.x, self.y, size[0], size[1])
        self.image = pygame.Surface(size)
        self.image.fill(self.color)
        self.size = size

    def update(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def spawn(self, screen, snakes, g):
        size = self.size
        n = True
        while n:
            x1 = random.randint(1, g)  # get a random row to spawn in
            self.x = (x1 - 1) * size[0]  # get the x of the row
            y1 = random.randint(1, 41)  # get a random line to spawn in
            self.y = y1 * size[1]  # get the y of the line
            x_list = []
            for i in range(len(snakes)):
                x_list.append(snakes[i].x)
                x_list.append(snakes[i].y)
            if not (x1 or y1) in x_list:  # test if the fruit isn't in a snake
                self.rect.update(self.x, self.y, size[0], size[1])
                screen.blit(self.image, (self.x, self.y))
                n = False
            else:  # redo
                n = True
        return self
