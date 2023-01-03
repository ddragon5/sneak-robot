import pygame
import sklearn

import create


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
        for t in range(len(group)):
            f += 1
            self.x += size[0]
            if f == mf:
                self.line += 1
                f = 0
                self.y += size[1]
                self.x = 0

        self.rect = pygame.Rect(self.x, self.y, size[0], size[1])
        self.image = pygame.draw.rect(screen, self.color, self.rect)
        self.size = size

    def update(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

