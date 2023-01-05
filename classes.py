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
            print("print")
            self.tag = ('snake', 'potrkyk')
        else:
            self.tag = ('floor')
            self.type = Spots.BLANK
        self.rect = pygame.Rect(self.x, self.y, size[0], size[1])
        self.image = pygame.draw.rect(screen, self.color, self.rect)
        self.size = size
        self.dir = 2  # 1 = up  2 = right  3 = down  4 = left

    def update(self, screen, slots_s, o, snakes, moved):
        running = True
        if not moved and (int(snakes[0].x + self.size[0]) != 690 or int(snakes[0].x)) != 0 and (
                self.tag[0] == 'snake' or self.tag == 'snake'):
            running = False
            moved = True
            for c in snakes:
                for l in slots_s:
                    if c.dir == 1:
                        if l.line == c.line - 1 and l.row == c.row:
                            if "head" in c.tag:
                                l.tag = ('snake', 'head', 1)
                                l.color = (138, 43, 226)
                                c.tag = 'floor'
                                snakes[0] = l
                            if 'body' in c.tag:
                                l.tag = ('snake', 'body', c.tag2)
                                l.color = (138, 43, 226)
                                l.dir = snakes[0].dir
                                inde = c.tag[2] - 1
                                snakes[inde] = [l]
                            if 'last' in c.tag:
                                l.tag = ('snake', 'last', c.tag[2])
                                l.color = (138, 43, 226)
                                l.dir = [c.tag[2] + 1].dir
                                c.tag = 'floor'
                    if c.dir == 2:
                        if [l].row == [c].row + 1 and [l].line == [c].line:
                            if "head" in [c].tag:
                                print('here h')
                                l.tag = ('snake', 'head', 1)
                                l.color = (138, 43, 226)
                                c.tag = 'floor'
                                snakes[0] = [l]
                            if 'body' in [c].tag:
                                print('here b')
                                [l].tag = ('snake', 'body', [c].tag[2])
                                [l].color = (138, 43, 226)
                                [l].dir = [0].dir
                                inde = [c].tag[2] - 1
                                snakes[inde] = [l]
                            if 'last' in [c].tag:
                                print('here l')
                                slots_s[l].tag = ('snake', 'last', [c].tag[2])
                                slots_s[l].color = (138, 43, 226)
                                slots_s[l].dir = [[c].tag[2] - 1].dir
                                [c].tag = 'floor'
                    if [c].dir == 3:
                        if slots_s[l].line == [c].line + 1 and l.row == [c].row:
                            if "head" in [c].tag:
                                [l].tag = ('snake', 'head', 1)
                                [l].color = (138, 43, 226)
                                [c].tag = 'floor'
                                snakes[0] = [l]
                            if 'body' in [c].tag:
                                [l].tag = ('snake', 'body', [c].tag[2])
                                [l].color = (138, 43, 226)
                                [l].dir = [0].dir
                                inde = [c].tag[2] - 1
                                snakes[inde] = [l]
                            if 'last' in [c].tag:
                                [l].tag = ('snake', 'last', [c].tag[2])
                                [l].color = (138, 43, 226)
                                [l].dir = [[c].tag[2] + 1].dir
                                [c].tag = 'floor'
                    if [c].dir == 4:
                        if [l].row == [c].row - 1 and [l].line == [c].line:
                            if "head" in [c].tag:
                                [l].tag = ('snake', 'head', 1)
                                [l].color = (138, 43, 226)
                                [c].tag = 'floor'
                                snakes[0] = [l]
                            if 'body' in [c].tag:
                                [l].tag = ('snake', 'body', [c].tag[2])
                                [l].color = (138, 43, 226)
                                [l].dir = [0].dir
                                inde = [c].tag[2] - 1
                                snakes[inde] = [l]
                            if 'last' in [c].tag:
                                l.tag = ('snake', 'last', [c].tag[2])
                                l.color = (138, 43, 226)
                                l.dir = [[c].tag[2] + 1].dir
                                c.tag = 'floor'
        if self.tag == 'floor':
            if self.line % 2 != 0:
                if self.row % 2 != 0:
                    self.color = (155, 206, 62)  # darker
                else:
                    self.color = (170, 215, 81)  # lighter
            else:
                if self.row % 2 == 0:
                    self.color = (155, 206, 62)  # darker
                else:
                    self.color = (170, 215, 81)  # lighter
        pygame.draw.rect(screen, self.color, self.rect)
        return slots_s, moved, snakes, running
