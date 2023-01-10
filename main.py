import torch
import pygame

import classes
import create
import time


def update(slots_s, slots_r, screen, snakes):
    screen = pygame.display.set_mode((create.width, create.height))
    create.create_backgound(screen)
    moved = False
    for i in range(len(slots_s)):
        slots_s, moved, snakes, running = slots_s[i].update(screen, slots_s, i, snakes, moved)
    # removing new tag
    for i in range(len(slots_s)):
        if slots_s[i].type == classes.Spots.HEAD or slots_s[i].type == classes.Spots.TAIL:
            if slots_s[i].new:
                slots_s[i].new = False
    return slots_s, running


def run(slots_s, slots_r, screen, snakes):
    running = True
    s = 0
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        slots_s, running = update(slots_s, slots_r, screen, snakes)
        pygame.display.update()
        s += 1
        print(s)
        clock.tick(10)


def main():
    screen = create.window()
    slots_s, slots_r, s = create.floor(screen)
    run(slots_s, slots_r, screen, s)


if __name__ == "__main__":
    main()
