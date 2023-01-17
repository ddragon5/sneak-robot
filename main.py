import pygame
import classes
import create
import misc


def update(screen, snakes, n_dir, fruits, g, f, score):
    screen = pygame.display.set_mode((create.width, create.height))
    Background_ = create.create_backgound(screen)
    moved = False
    # update fruits
    for i in range(len(fruits)):
        n = fruits[i]
        n.update(screen)
    # update the position of snakes
    count = 0
    for i in range(len(snakes)):
        n = snakes[i]
        snakes, count = n.update(screen, snakes, score, count)
    for i in range(len(snakes)):
        n = snakes[i]
        n.moved = False
    # check if player was killed
    n = snakes[len(snakes) - 1]
    running, fruits, snakes, score = n.check(snakes, Background_, fruits, screen, g, score)
    running = not running

    return snakes, running, fruits, score


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
    score = 0
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
                if event.key == pygame.K_m:
                    snakes = misc.longer(snakes, size, g, screen)
                    score += 1

        if len(snakes) >= 4:
            print(snakes[0].type, snakes[0].x, snakes[0].y)
        snakes[len(snakes) - 1].dir = n_dir
        snakes, running, fruits, score = update(screen, snakes, n_dir, fruits, g, f, score)
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
