import torch
import pygame

import classes
import create
import time


def update(slots_s, slots_r, screen, snakes, n_dir):
    screen = pygame.display.set_mode((create.width, create.height))
    create.create_backgound(screen)
    moved = False
    n = snakes[len(snakes) - 1]
    running, head_moved = n.check(snakes)
    for i in range(len(slots_s)):
        slots_s, moved, snakes, running = slots_s[i].update(screen, slots_s, i, snakes, moved, n_dir, running)

    for i in range(len(snakes)):
        # removing new tag
        if slots_s[i].type == classes.Spots.HEAD or slots_s[i].type == classes.Spots.TAIL:
            if slots_s[i].new:
                slots_s[i].new = False

        # checking if the snake has been killed
    return slots_s, running


def run(slots_s, slots_r, screen, snakes):
    running = True
    n_dir = snakes[len(snakes)-1].dir
    dir = snakes[len(snakes)-1].dir
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # test if a key is preset
            if event.type == pygame.KEYDOWN:
                # test if the up arrow or the w key are preset
                if event.key == (pygame.K_UP or pygame.K_w):
                    n_dir = classes.Dir.UP
                # test if the down arrow or the s key are preset
                if event.key == (pygame.K_DOWN or pygame.K_s):
                    n_dir = classes.Dir.DOWN
                # right arrow and d key
                if event.key == (pygame.K_RIGHT or pygame.K_d):
                    n_dir = classes.Dir.RIGHT
                # left arrow and a key
                if event.key == (pygame.K_LEFT or pygame.K_a):
                    n_dir = classes.Dir.LEFT

        slots_s, running = update(slots_s, slots_r, screen, snakes, n_dir)
        pygame.display.update()
        clock.tick(5)


def main():
    screen = create.window()
    slots_s, slots_r, s = create.floor(screen)
    run(slots_s, slots_r, screen, s)


if __name__ == "__main__":
    main()