import pygame
import classes
import create


def update(screen, snakes, n_dir, fruits, g, f):
    screen = pygame.display.set_mode((create.width, create.height))
    Background_ = create.create_backgound(screen)
    moved = False
    # update fruits
    for i in range(len(fruits)):
        n = fruits[i]
        n.update(screen)
    # update the position of snakes
    for i in range(len(snakes)):
        n = snakes[i]
        snakes = n.update(screen, snakes)
    # check if player was killed
    n = snakes[len(snakes) - 1]
    running, fruits, snakes = n.check(snakes, Background_, fruits, screen, g)
    running = not running

    return snakes, running, fruits


def run(screen, size, snakes, fruits, g, f):
    running = True
    al_dir = []
    n_dir = snakes[len(snakes)-1].dir
    y = len(snakes)  # len of snake
    for i in range(y):
        al_dir.append(snakes[i].dir)
    clock = pygame.time.Clock()
    u = -1
    fps = 1
    while running:
        u += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # test if a key is preset
            if event.type == pygame.KEYDOWN:
                # test if the up arrow or the w key are preset
                if event.key == (pygame.K_UP or pygame.K_w):
                    n_dir = classes.Dir.DOWN
                # test if the down arrow or the s key are preset
                if event.key == (pygame.K_DOWN or pygame.K_s):
                    n_dir = classes.Dir.UP
                # right arrow and d key
                if event.key == (pygame.K_RIGHT or pygame.K_d):
                    n_dir = classes.Dir.RIGHT
                # left arrow and a key
                if event.key == (pygame.K_LEFT or pygame.K_a):
                    n_dir = classes.Dir.LEFT

                if event.key == pygame.K_l:
                    fps += 1
                if event.key == pygame.K_j:
                    fps -= 1
                    if fps <= 0:
                        fps = 1

        snakes[len(snakes) - 1].dir = n_dir
        snakes, running, fruits = update(screen, snakes, n_dir, fruits, g, f)
        pygame.display.update()
        clock.tick(fps)


def main():
    screen = create.window()
    size, g, f = create.size_squares(screen)
    snakes = create.create_snakes(size, g, f)
    fruits = create.create_fruit(size, g, f, snakes)
    run(screen, size, snakes, fruits, g, f)


if __name__ == "__main__":
    main()
