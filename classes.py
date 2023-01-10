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


class tails(pygame.sprite.Sprite):
    def __init__(self, size, group, screen):
        super().__init__()
        if len(group) % 2 != 0:
            self.color = (155, 206, 62)  # darker
        else:
            self.color = (170, 215, 81)  # lighter
        self.x = 0
        self.y = 0
        f = 0
        mf = create.width / size[0]
        if mf % 2 == 0:
            mf += 1
        self.line = 1
        self.row = 1
        for t in range(len(group)):
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
        if self.line == self.mg / 2 and (self.row == 12 or self.row == 13 or self.row == 11):
            self.tag = ('snake', 'potrkyk')
            self.new = True
        else:
            self.tag = ('floor')
            self.type = Spots.BLANK
        self.rect = pygame.Rect(self.x, self.y, size[0], size[1])
        pygame.draw.rect(screen, self.color, self.rect)
        self.size = size
        self.dir = 2  # 1 = up  2 = right  3 = down  4 = left

    def update(self, screen, slots_s, o, snakes, moved):
        running = True
        if not moved and (int(snakes[0].x + self.size[0]) != 690 or int(snakes[0].x)) != 0:
            running = True
            moved = True
            head_moved = False
            tail_moved = False
            body_moved = 0
            has_m = [head_moved, tail_moved, body_moved]
            n = 0
            for i in range(len(snakes)):
                c = snakes[i]
                for n in range(len(slots_s)):
                    l = slots_s[n]
                    if c.dir == 1:
                        if l.line == c.line - 1 and l.row == c.row:
                            if (c.type == Spots.HEAD and has_m[0] == True) or (
                                    c.type == Spots.BODY and has_m[2] == len(snakes) - 2) or (
                                    c.type == Spots.TAIL and has_m[1] == True):
                                move(c, l, snakes, has_m)
                            else:
                                c, l, snakes, has_m = move(c, l, snakes, has_m)
                    if c.dir == 2:
                        if l.row == c.row + 1 and l.line == c.line:
                            n += 1
                            snakes, has_m, slots_s = move(c, l, snakes, has_m, slots_s)
                    if c.dir == 3:
                        if l.line == c.line + 1 and l.row == c.row:
                            if (c.type == Spots.HEAD and has_m[0] == True) or (
                                    c.type == Spots.BODY and has_m[2] == len(snakes) - 2) or (
                                    c.type == Spots.TAIL and has_m[1] == True):
                                move(c, l, snakes, has_m)
                            else:
                                c, l, snakes, has_m = move(c, l, snakes, has_m)
                    if c.dir == 4:
                        if l.row == c.row - 1 and l.line == c.line:
                            if (c.type == Spots.HEAD and has_m[0] == True) or (
                                    c.type == Spots.BODY and has_m[2] == len(snakes) - 2) or (
                                    c.type == Spots.TAIL and has_m[1] == True):
                                move(c, l, snakes, has_m)
                            else:
                                c, l, snakes, has_m = move(c, l, snakes, has_m)

                    if has_m[0] and has_m[1] and has_m[2] == 1:
                        break
                if has_m[0] and has_m[1] and has_m[2] == 1:
                    break
        if self.type == Spots.BLANK:
            self.color = get_color(self)
        pygame.draw.rect(screen, self.color, self.rect)
        return slots_s, moved, snakes, running


def move(c, l, snakes, has_m, s):
    if c.type == Spots.HEAD:
        if has_m[0] == True:
            g = snakes, has_m
            return snakes, has_m, s
        else:
            l.tag = ('snake', 'head', 1)
            l.new = True
            l.color = (138, 43, 226)
            l.type = Spots.HEAD
            c.tag = ('snake', 'body', 2)
            c.type = Spots.BODY
            snakes[len(snakes)-1] = l
            snakes[len(snakes)-2] = c
            has_m[0] = True
            g = snakes, has_m
            return snakes, has_m, s
    if c.type == Spots.BODY:
        if has_m[2] >= len(snakes) - 2:
            g = snakes, has_m
            print(type(snakes), type(has_m))
            return snakes, has_m, s
        else:
            has_m[2] += 1
            print(type(snakes), type(has_m))
            return snakes, has_m, s
    if c.type == Spots.TAIL:
        if has_m[1] == True:
            g = snakes, has_m
            print(type(snakes), type(has_m))
            return snakes, has_m, s
        else:
            c.tag = 'floor'
            c.type = Spots.BLANK
            c.color = get_color(c)
            s[c.index] = c
            has_m[1] = True
            l.type = Spots.TAIL
            l.new = True
            l.tag = ('snake', 'last', 3)
            snakes[0] = l
            g = snakes, has_m
            print(type(snakes), type(has_m))
            return snakes, has_m

def get_color(n):
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
