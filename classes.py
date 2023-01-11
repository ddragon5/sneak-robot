import pygame
import torch
import create
from enum import Enum


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


class Tail_Dir:
    def __init__(self, max, group):
        self.max = max
        self.dir = group[0]
        self.group = group

    def __next__(self, n_dir):
        if self.dir == max:
            raise StopIteration
        self.group.pop(0)
        self.group.append(n_dir)
        self.dir = self.group[0]
        return self.dir


class tails(pygame.sprite.Sprite):
    def __init__(self, size, group, screen):
        super().__init__()
        self.x = 0
        self.y = 0
        f = 0
        mf = create.width / size[0]
        if mf % 2 == 0:
            mf += 1
        self.line = 1
        self.row = 1
        for i in range(len(group)):
            f += 1
            self.x += size[0]
            self.row += 1
            if f == mf:
                self.line += 1
                f = 0
                self.row = 1
                self.y += size[1]
                self.x = 0

        self.mg = create.height / size[1]
        self.mf = mf
        self.mg = int(self.mg)
        tail_point = 11
        snake_len = 4
        possible_row = []
        for i in range(snake_len):
            possible_row.append(tail_point)
            tail_point += 1
        if self.line == self.mg / 2 and self.row in possible_row:
            if self.row == possible_row[0]:
                self.type = Spots.TAIL
                self.tag = ('snake', 'last', snake_len)

            if self.row != (possible_row[0] or possible_row[snake_len - 1]):
                self.type = Spots.BODY
                self.tag = ('snake', 'body', 2)

            if self.row == possible_row[snake_len - 1]:
                self.type = Spots.HEAD
                self.tag = ('snake', 'head', 1)

        else:
            self.tag = ('floor')
            self.type = Spots.BLANK
        self.color = get_color(self)
        self.x = int(self.x)
        self.rect = pygame.Rect(self.x, self.y, size[0], size[1])
        pygame.draw.rect(screen, self.color, self.rect)
        self.size = size
        self.dir = Dir.RIGHT
        self.dir_value = Dir.RIGHT.value
        self.dir_s = self.dir
        self.len = snake_len

    def update(self, screen, slots_s, o, snakes, moved, n_dir, running):
        if not moved and self.type.value >= 1 and self.type.value != 4:
            running = running
            tail_moved = False
            head_moved = False
            r = 5
            q = 10
            body_moved = 0
            has_m = [head_moved, tail_moved, body_moved]

            c = self
            c.dir = n_dir
            c.dir_value = c.dir.value
            y = get_dir(slots_s, c, snakes)

            if c.type == Spots.TAIL:
                snakes, has_m, slots_s, self = move(c, y, snakes, has_m, slots_s, q)
            else:
                if c.type != (Spots.BLANK or Spots.FRUIT):
                    snakes, has_m, slots_s, self = move(c, r, snakes, has_m, slots_s, q)
            if has_m[0] and has_m[1] and has_m[2] >= len(snakes) - 2:
                moved = True

        self.color = get_color(self)
        pygame.draw.rect(screen, self.color, self.rect)
        return slots_s, moved, snakes, running

    def check(self, snakes):
        is_dead = False
        head_moved = False
        for i in range(len(snakes) - 2):
            n = snakes[i]
            i = snakes[i].rect
            if self.rect.colliderect(i):
                is_dead = True
                print(n.type, ' ', n.index, n.line, n.row)
                if n == snakes[len(snakes) - 2]:
                    print('jysergdf')

        if (self.x >= 690 or int(self.x) <= 0) or (
                int(self.y + self.size[1]) >= 600 or (int(self.y + self.size[1]) == 15 and self.dir == Dir.UP)):
            is_dead = True
        # print(self.rect.colliderect(i))
        return not is_dead, head_moved


def move(c, y, snakes, has_m, s, q):
    redo = True
    while redo:
        try:
            if c.type == Spots.HEAD:
                if has_m[0]:
                    g = snakes, has_m
                    redo = False
                    return snakes, has_m, s
                else:
                    y.tag = ('snake', 'head', 1)
                    y.new = True
                    y.color = (138, 43, 226)
                    y.type = Spots.HEAD
                    c.tag = ('snake', 'body', 2)
                    c.type = Spots.BODY
                    snakes[len(snakes) - 1] = y
                    snakes[len(snakes) - 2] = c
                    has_m[0] = True
                    redo = False
                    g = snakes, has_m
                    return snakes, has_m, s, c
            if c.type == Spots.BODY:
                if has_m[2] >= len(snakes) - 2:
                    g = snakes, has_m
                    redo = False
                    return snakes, has_m, s, c
                else:
                    has_m[2] += 1
                    redo = False
                    return snakes, has_m, s, c
            if c.type == Spots.TAIL:
                if has_m[1]:
                    s[c.index].color = (74, 176, 224)
                    g = snakes, has_m
                    redo = False
                    return snakes, has_m, s, c
                else:
                    r = y
                    r.tag = ('snake', 'last', len(snakes))
                    r.new = True
                    r.color = get_color(r)
                    r.type = Spots.TAIL
                    r.dir_s = c.dir_s
                    snakes[0] = r
                    c.tag = ('floor')
                    c.type = Spots.BLANK
                    c.color = get_color(c)
        
                    has_m[1] = True
                    g = snakes, has_m
                    redo = False
                    return snakes, has_m, s, c
        except AttributeError:
            redo = True
            print('rtegg')
            y = get_dir(s, c)
    print('gtrs')
    return snakes, has_m, s, c

def get_color(n):
    # the color of the background
    if n.type.value == 0:
        if n.line % 2 != 0:
            if n.row % 2 != 0:
                return (155, 206, 62)  # darker
            else:
                return (170, 215, 81)  # lighter
        else:
            if n.row % 2 == 0:
                return (155, 206, 62)  # darker
            else:
                return (170, 215, 81)  # lighter
    # the color of the snake
    if n.type == Spots.HEAD:
        return (138, 43, 226)

    if n.type == Spots.BODY:
        return (187, 54, 105)

    if n.type == Spots.TAIL:
        return (252, 42, 232)


def get_dir(slots_s, c, snakes):
    for n in range(len(slots_s)):
        l = slots_s[n]
        if c.index == 939:
            c = snakes[len(snakes)-2]
        if c.dir == Dir.UP:
            if l.line == c.line - 1 and l.row == c.row:
                return l
        if c.dir == Dir.DOWN:
            if l.line == c.line + 1 and l.row == c.row:
                return l
        if c.dir == Dir.RIGHT:
            if l.row == c.row + 1 and l.line == c.line:
                return l
        if c.dir == Dir.LEFT:
            if l.row == c.row - 1 and l.line == c.line:
                return l

