import pygame
import create
from enum import Enum
from misc import get_dir, get_color
from move import move


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
        self.x = int(self.x)
        self.rect = pygame.Rect(self.x, self.y, size[0], size[1])
        self.size = size
        self.dir = Dir.RIGHT
        self.dir_value = Dir.RIGHT.value
        self.dir_s = self.dir

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

########################################################################################################################

class snake(pygame.sprite.Sprite):
    def __init__(self, snake, size):
        super.__init__()
        self.color = (236, 231, 2)  # color of the snake
        # find place on the grid
        line = create.height // 2  # קו ישר
        row = 11  # טור
        for i in range(len(snake)):
            row += 1
            self.type = Spots[i]
        self.gir_pos = (line, row)
        # find x and y
        self.x = row-1 * size[0]
        self.y = line * size[1]
        self.dir = Dir.RIGHT
        self.rect = pygame.Rect(self.x, self.y, size[0], size[1])

    def update(self, size, screen):
        if self.dir == Dir.RIGHT:
            self.x += size[0]
        if self.dir == Dir.LEFT:
            self.x -= size[0]
        if self.dir == Dir.UP:
            self.y += size[1]
        if self.dir == Dir.DOWN:
            self.y -= size[1]
        pygame.draw.rect(screen, self.color, self.rect)

    def check(self):
        is_dead = False
