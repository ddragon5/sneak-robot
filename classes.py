import pygame
import torch
import create


class tails(pygame.sprite.Sprite):
    def __init__(self, size, group, screen):
        super().__init__()
        if len(group) % 2 != 0:
            self.color = (155, 206, 62)  # darker
        else:
            self.color = (170, 215, 81)  # lighter

        self.len = 3
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
            self.color = (138, 43, 226)
            self.tag = ('snake', 'body', 2)
            if self.line == self.mg / 2 and self.row == 11:
                self.tag = ('snake', 'last', 3)
                self.new = False
            if self.line == self.mg / 2 and self.row == 13:
                self.tag = ('snake', 'head', 1)
                self.new = False
        else:
            self.tag = ('floor')
        self.rect = pygame.Rect(self.x, self.y, size[0], size[1])
        self.image = pygame.draw.rect(screen, self.color, self.rect)
        self.size = size
        self.dir = 2  # 1 = up  2 = right  3 = down  4 = left

    def update(self, screen, slots_s, o, snakes, moved):
        if not moved and (int(snakes[0].x+self.size[0]) != 690 or int(snakes[0].x)) != 0 and (self.tag[0] == 'snake' or self.tag == 'snake'):
            moved = True
            for c in range(len(snakes)):
                for l in range(len(slots_s)):
                    if snakes[c].dir == 1:
                        if slots_s[l].line == snakes[c].line - 1 and slots_s[l].row == snakes[c].row:
                            if "head" in snakes[c].tag:
                                slots_s[l].tag = ('snake', 'head', 1)
                                slots_s[l].color = (138, 43, 226)
                                snakes[c].tag = 'floor'
                                snakes[0] = slots_s[l]
                            if 'body' in snakes[c].tag:
                                slots_s[l].tag = ('snake', 'body', snakes[c].tag[2])
                                slots_s[l].color = (138, 43, 226)
                                slots_s[l].dir = snakes[0].dir
                                inde = snakes[c].tag[2] - 1
                                snakes[inde] = slots_s[l]
                            if 'last' in snakes[c].tag:
                                slots_s[l].tag = ('snake', 'last', snakes[c].tag[2])
                                slots_s[l].color = (138, 43, 226)
                                slots_s[l].dir = snakes[snakes[c].tag[2] + 1].dir
                                snakes[c].tag = 'floor'
                    if snakes[c].dir == 2:
                        if slots_s[l].row == snakes[c].row + 1 and slots_s[l].line == snakes[c].line:
                            print('here')
                            if "head" in snakes[c].tag:
                                slots_s[l].tag = ('snake', 'head', 1)
                                slots_s[l].color = (138, 43, 226)
                                snakes[c].tag = 'floor'
                                snakes[0] = slots_s[l]
                            if 'body' in snakes[c].tag:
                                slots_s[l].tag = ('snake', 'body', snakes[c].tag[2])
                                slots_s[l].color = (138, 43, 226)
                                slots_s[l].dir = snakes[0].dir
                                inde = snakes[c].tag[2] - 1
                                snakes[inde] = slots_s[l]
                            if 'last' in snakes[c].tag:
                                slots_s[l].tag = ('snake', 'last', snakes[c].tag[2])
                                slots_s[l].color = (138, 43, 226)
                                slots_s[l].dir = snakes[snakes[c].tag[2]-1].dir
                                snakes[c].tag = 'floor'
                    if snakes[c].dir == 3:
                        if slots_s[l].line == snakes[c].line + 1 and slots_s.row == snakes[c].row:
                            if "head" in snakes[c].tag:
                                slots_s[l].tag = ('snake', 'head', 1)
                                slots_s[l].color = (138, 43, 226)
                                snakes[c].tag = 'floor'
                                snakes[0] = slots_s[l]
                            if 'body' in snakes[c].tag:
                                slots_s[l].tag = ('snake', 'body', snakes[c].tag[2])
                                slots_s[l].color = (138, 43, 226)
                                slots_s[l].dir = snakes[0].dir
                                inde = snakes[c].tag[2] - 1
                                snakes[inde] = slots_s[l]
                            if 'last' in snakes[c].tag:
                                slots_s[l].tag = ('snake', 'last', snakes[c].tag[2])
                                slots_s[l].color = (138, 43, 226)
                                slots_s[l].dir = snakes[snakes[c].tag[2] + 1].dir
                                snakes[c].tag = 'floor'
                    if snakes[c].dir == 4:
                        if slots_s[l].row == snakes[c].row - 1 and slots_s[l].line == snakes[c].line:
                            if "head" in snakes[c].tag:
                                slots_s[l].tag = ('snake', 'head', 1)
                                slots_s[l].color = (138, 43, 226)
                                snakes[c].tag = 'floor'
                                snakes[0] = slots_s[l]
                            if 'body' in snakes[c].tag:
                                slots_s[l].tag = ('snake', 'body', snakes[c].tag[2])
                                slots_s[l].color = (138, 43, 226)
                                slots_s[l].dir = snakes[0].dir
                                inde = snakes[c].tag[2] - 1
                                snakes[inde] = slots_s[l]
                            if 'last' in snakes[c].tag:
                                slots_s[l].tag = ('snake', 'last', snakes[c].tag[2])
                                slots_s[l].color = (138, 43, 226)
                                slots_s[l].dir = snakes[snakes[c].tag[2] + 1].dir
                                snakes[c].tag = 'floor'
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
        return slots_s, moved, snakes

