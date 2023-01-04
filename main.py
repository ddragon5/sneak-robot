import torch
import pygame
import create
import time


def update(slots_s, slots_r, screen, snakes):
    screen = pygame.display.set_mode((create.width, create.height))
    create.create_backgound(screen)
    for o in range(len(slots_s)):
        slots_s = slots_s[o].update(screen, slots_s, o, snakes)
        if slots_s[o].tag[1] == 'head' or 'last' in slots_s[o].tag:
            if slots_s[o].new:
                slots_s[o].new = False

    return slots_s



def run(slots_s, slots_r, screen, snakes):
    running = True
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        slots_s = update(slots_s, slots_r, screen, snakes)
        pygame.display.update()
        clock.tick(1)


def main():
    screen = create.window()
    slots_s, slots_r, s = create.floor(screen)
    run(slots_s, slots_r, screen, s)


if __name__ == "__main__":
    main()

