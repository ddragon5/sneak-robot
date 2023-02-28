import time

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
    def __init__(self, snakes, size, g, f, skin, start_row=11, start_line=41 // 2):
        super(pygame.sprite.Sprite, self).__init__()
        self.size = size
        # find place on the grid
        line = start_line  # קו ישר
        row = start_row  # טור
        for i in range(len(snakes)):
            row += 1
        self.type = Spots.BLANK
        if row == start_row:
            self.type = Spots.TAIL
        if row == 13:
            self.type = Spots.HEAD
        if row == 12:
            self.type = Spots.BODY
        self.new = False
        self.gir_pos = (line, row)
        # find x and y
        self.x = (row - 1) * size[0]
        self.y = line * size[1]
        self.dir = Dir.RIGHT
        if self.type == Spots.BLANK:
            self.dir = snakes[0].dir
            self.x = snakes[0].x
            self.y = snakes[0].y
            self.new = True
            self.type = Spots.BODY

        self.color = misc.get_color(self, skin)
        self.row = row
        self.line = line
        self.index = len(snakes)
        self.rect = pygame.Rect(self.x, self.y, size[0], size[1])
        self.image = pygame.Surface(size)
        self.image.fill(self.color)
        self.s_dir = self.dir
        self.moved = False
        self.id = "x and y: ", self.x, self.y, self.dir, 'index: ', self.index, self.rect, self.type

    def update(self, screen, snakes, score, count, i, n_dir, dir_all):
        size = self.size
        if self.type == Spots.TAIL:
            if self.dir == Dir.RIGHT:
                self.row += 1
                self.x += 15
            if self.dir == Dir.LEFT:
                self.row -= 1
                self.x -= 15
            if self.dir == Dir.UP:
                self.line -= 1
                self.y += 15
            if self.dir == Dir.DOWN:
                self.line += 1
                self.y -= 15

        if self.type != Spots.TAIL and not self.moved or (self == snakes[len(snakes)-2] and self.moved and count > 2):
            count += 1
            calc = 15
            if self.dir == Dir.RIGHT:
                self.x += calc
                self.row += 1
            if self.dir == Dir.LEFT:
                self.row -= 1
                self.x -= calc
            if self.dir == Dir.UP:
                self.y += calc
                self.line -= 1
            if self.dir == Dir.DOWN:
                self.line += 1
                self.y -= calc

        self.x = int(self.x)
        self.y = int(self.y)
        self.gir_pos = (self.line, self.row)
        self.rect.update(self.x, self.y, size[0], size[1])
        screen.blit(self.image, (self.x, self.y))
        self.moved = True

        try:
            self.dir = dir_all[i+1]
        except IndexError:
            pass

        snakes[i] = self
        return snakes, count, dir_all

    def check(self, snakes, Background_, fruits, screen, g, score, skin):
        Background_rect = Background_.get_rect()
        is_dead = False
        # checking if out of bonds
        if self.x > 690 or self.x < 0 or self.y > 600 or self.y < 0:
            is_dead = True
            print('cause of death out of bounds')
            return is_dead, fruits, snakes, score
        # checking if he collided with him self except if he hit his neck
        for i in range(len(snakes) - 2):
            s = snakes[i]
            r = s.rect
            if self.rect.contains(r):
                is_dead = True  # True or False
                print("cause of death inside self")
                print('specially', str(s.type), str(i), str(s.gir_pos), 'was in ', str(self.type), str(self.index), str(self.gir_pos))
                return is_dead, fruits, snakes, score
        # checking if the snake has eaten a fruit
        for i in range(len(fruits)):
            t = fruits[i]
            if self.rect.contains(t.rect):
                t = t.spawn(screen, snakes, g)
                fruits[i] = t
                snakes = misc.longer(snakes, self.size, g, screen, skin)
                score += 1
        return is_dead, fruits, snakes, score

########################################################################################################################


class fruit(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        super(pygame.sprite.Sprite, self).__init__()
        self.type = Spots.FRUIT
        self.x = x
        self.y = y
        self.color = misc.get_color(self)
        self.rect = pygame.Rect(self.x, self.y, size[0], size[1])
        self.image = pygame.Surface(size)
        self.image.fill(self.color)
        self.size = size

    def update(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def spawn(self, screen, snakes, g):
        size = self.size
        redo = True
        while redo:
            x1 = random.randint(1, g)  # get a random row to spawn in
            self.x = (x1 - 1) * size[0]  # get the x of the row
            y1 = random.randint(1, 40)  # get a random line to spawn in
            self.y = y1 * size[1]  # get the y of the line
            self.rect.update(self.x, self.y, size[0], size[1])
            screen.blit(self.image, (self.x, self.y))
            redo1 = False
            # test if the fruit isn't in a snake
            for i in range(len(snakes)):
                n = snakes[i]
                if n.rect.contains(self.rect):
                    redo1 = True
            redo = redo1
        return self


########################################################################################################################


class Button():
    def __init__(self, image, pos, hovering_image, color_key):
        self.image = image
        self.x = pos[0]
        self.y = pos[1]
        self.pos = (self.x, self.y)
        self.hovering_image = hovering_image
        self.colorkey = color_key
        self.image.set_colorkey(color_key)

    def update(self, screen, chosen):
        if not chosen:
            self.image.set_colorkey(self.colorkey)
            screen.blit(self.image, self.pos)
        if chosen:
            color_key = self.colorkey
            r = color_key[0]
            e = color_key[1]
            g = color_key[2]
            e += 4
            color_key = (r, e, g)
            self.image.set_colorkey(color_key)
            screen.blit(self.hovering_image, self.pos)
