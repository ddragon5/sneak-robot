import pygame
import classes
import create
import misc

width = 690  # 17 slots 53 pixel each
height = 600  # 15 slots 40 pixel each


def update(screen, snakes, n_dir, fruits, g, f, score):
    dir_all = []
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
        dir_all.append(n.dir)

    for i in range(len(snakes)):
        n = snakes[i]
        snakes, count, dir_all = n.update(screen, snakes, score, count, i, n_dir, dir_all)

    # check if player was killed
    n = snakes[len(snakes) - 1]
    running, fruits, snakes, score = n.check(snakes, Background_, fruits, screen, g, score)
    running = not running

    for i in range(len(snakes)):
        n = snakes[i]
        n.moved = False
        snakes[i].type = classes.Spots.BLANK
        if i == 0:
            snakes[i].type = classes.Spots.TAIL
        if i == (len(snakes) - 1):
            snakes[i].type = classes.Spots.HEAD
        if n.type == classes.Spots.BLANK:
            snakes[i].type = classes.Spots.BODY
    pygame.font.init()
    Score_font = pygame.font.SysFont('arialblack', 40)
    Score_COL = (255, 255, 255)
    Score_dis = Score_font.render(str(score), True, Score_COL)
    rect = Score_dis.get_rect()
    rect.center = width/2-30, 20
    screen.blit(Score_dis, rect.center)

    return snakes, running, fruits, score


def run(screen, size, snakes, fruits, g, f):
    pygame.init()
    game_loop = False
    start_menu = True
    running = True
    al_dir = []
    super_difficulty = False
    n_dir = classes.Dir.RIGHT
    y = len(snakes)  # len of snake
    for i in range(y):
        al_dir.append(snakes[i].dir)
    clock = pygame.time.Clock()
    u = -1
    if super_difficulty:
        fps = 0
    else:
        fps = 10
    score = 0
    pygame.init()
    while running:
        while start_menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        game_loop = True
                        start_menu = False

            screen = pygame.display.set_mode((create.width, create.height))
            Background_ = create.create_backgound(screen)


            # title
            pygame.font.init()
            font = pygame.font.SysFont("arialblack", 40)
            TEXT_COL = (50, 50, 50)
            TEXT = font.render("WELCOME TO SNAKE", True, TEXT_COL)
            screen.blit(TEXT, (115 - 7.5, 20))

            #PLAY_BUTTON = classes.Button()

            pygame.display.update()
            clock.tick(fps)

        # reset pos
        snakes = create.create_snakes(size, g, f)
        fruits = create.create_fruit(size, g, f, snakes)
        n_dir = classes.Dir.RIGHT
        # reset score
        score = 0

        while game_loop:
            u += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                # test if a key is preset
                if event.type == pygame.KEYDOWN:
                    # test if the up arrow or the w key are preset
                    if event.key == (pygame.K_UP or pygame.K_w) and n_dir != classes.Dir.UP:
                        n_dir = classes.Dir.DOWN
                    # test if the down arrow or the s key are preset
                    if event.key == (pygame.K_DOWN or pygame.K_s) and n_dir != classes.Dir.DOWN:
                        n_dir = classes.Dir.UP
                    # right arrow and d key
                    if event.key == (pygame.K_RIGHT or pygame.K_d) and n_dir != classes.Dir.LEFT:
                        n_dir = classes.Dir.RIGHT
                    # left arrow and a key
                    if event.key == (pygame.K_LEFT or pygame.K_a) and n_dir != classes.Dir.RIGHT:
                        n_dir = classes.Dir.LEFT

                    if event.key == pygame.K_l:
                        fps += 1
                    if event.key == pygame.K_j:
                        fps -= 1
                        if fps <= 0:
                            if super_difficulty:
                                pass
                            else:
                                fps = 0
                    if event.key == pygame.K_m:
                        snakes = misc.longer(snakes, size, g, screen)
                        score += 1

            snakes[score + 2].dir = n_dir

            snakes, game_loop, fruits, score = update(screen, snakes, n_dir, fruits, g, f, score)
            start_menu = not game_loop
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
