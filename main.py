import sklearn
import pygame
import create


def update(slots_s, slots_r, screen):
    screen = pygame.display.set_mode((create.width, create.height))
    create.create_backgound(screen)
    for o in range(len(slots_s)):
        slots_s[o].update(screen)


def run(slots_s, slots_r, screen):
    running = True
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        update(slots_s, slots_r, screen)
        pygame.display.update()
        clock.tick(60)


def main():
    screen = create.window()
    slots_s, slots_r = create.floor(screen)
    run(slots_s, slots_r, screen)


if __name__ == "__main__":
    main()
