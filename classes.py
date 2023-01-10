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

    def update(self, screen, slots_s, o, snakes, moved, n_dir, running):
        if not moved:
            running = running
            moved = True
            tail_moved = False
            head_moved = False
            r = 5
            body_moved = 0
            has_m = [head_moved, tail_moved, body_moved]
            for i in range(len(snakes)):
                c = snakes[i]
                c.dir = n_dir
                c.dir_value = c.dir.value
                for n in range(len(slots_s)):
                    l = slots_s[n]
                    if c.type == Spots.TAIL:
                        if c.dir == Dir.UP:
                            if l.line == c.line + 1 and l.row == c.row:
                                q = l
                        if c.dir == Dir.DOWN:
                            if l.line == c.line - 1 and l.row == c.row:
                                q = l
                        if c.dir == Dir.RIGHT:
                            if l.row == c.row - 1 and l.line == c.line:
                                q = l
                        if c.dir == Dir.LEFT:
                            if l.row == c.row + 1 and l.line == c.line:
                                q = l

                    if c.dir == Dir.UP:
                        if l.line == c.line - 1 and l.row == c.row:
                            r = l
                    if c.dir == Dir.DOWN:
                        if l.line == c.line + 1 and l.row == c.row:
                            r = l
                    if c.dir == Dir.RIGHT:
                        if l.row == c.row + 1 and l.line == c.line:
                            r = l
                    if c.dir == Dir.LEFT:
                        if l.row == c.row - 1 and l.line == c.line:
                            r = l

                try:
                    snakes, has_m, slots_s = move(c, r, snakes, has_m, slots_s)
                except TypeError:
                    pass
            pygame.draw.rect(screen, c.color, c.rect)
        self.color = get_color(self)
        pygame.draw.rect(screen, self.color, self.rect)
        return slots_s, moved, snakes, running

    def check(self, snakes):
        is_dead = False
        head_moved = False
        for i in range(len(snakes) - 1):
            n = i
            i = snakes[i].rect
            if self.rect.colliderect(i):
                is_dead = True
                print('grefsdgv')
                if n == snakes[len(snakes) - 2]:
                    print('jysergdf')

        if (self.x >= 690 or int(self.x) <= 0) or (
                int(self.y + self.size[1]) >= 600 or (int(self.y + self.size[1]) == 15 and self.dir == Dir.UP)):
            is_dead = True
        # print(self.rect.colliderect(i))
        return not is_dead, head_moved


def move(c, l, snakes, has_m, s, q=10):
    if c.type == Spots.HEAD:
        if has_m[0] == True or (l.type == Spots.BODY and l.tag[2] == 2):
            g = snakes, has_m
            return snakes, has_m, s
        else:
            l.tag = ('snake', 'head', 1)
            l.new = True
            l.color = (138, 43, 226)
            l.type = Spots.HEAD
            c.tag = ('snake', 'body', 2)
            c.type = Spots.BODY
            snakes[len(snakes) - 1] = l
            snakes[len(snakes) - 2] = c
            has_m[0] = True
            g = snakes, has_m
            return snakes, has_m, s
    if c.type == Spots.BODY:
        if has_m[2] >= len(snakes) - 2:
            g = snakes, has_m
            return snakes, has_m, s
        else:
            has_m[2] += 1
            return snakes, has_m, s
    if c.type == Spots.TAIL:
        if has_m[1]:
            g = snakes, has_m
            return snakes, has_m, s
        else:
            r = l
            r.tag = ('snake', 'last', len(snakes))
            r.new = True
            r.color = (252, 42, 232)
            r.type = Spots.TAIL
            snakes[1] = r
            c.tag = ('floor')
            c.type = Spots.BLANK
            c.color = get_color(c)

            has_m[1] = True
            g = snakes, has_m
            return snakes, has_m, s


#            t = c
#            r = snakes[1]
#            f = r
#            # r -> t
#            if f is r:
#                r.type = c.type
#                r.new = True
#                r.tag = c.tag
#                r.color = c.color
#                snakes[0] = r
#                s[r.index] = r
#
#            # c -> blank
#            if t is c:
#                c.tag = 'floor'
#                c.type = Spots.BLANK
#                c.color = get_color(c)
#                s[c.index] = c
#            if q != 10:
#                return snakes, has_m, s, q

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
