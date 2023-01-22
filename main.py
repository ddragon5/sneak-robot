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
    rect.center = width / 2 - 30, 20
    screen.blit(Score_dis, rect.center)

    return snakes, running, fruits, score


def run(screen, size, snakes, fruits, g, f):
    pygame.init()
    game_loop = False
    start_menu = True
    settings_menu = False
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
    chosen = 0  # | 0 for start | 1 for settings | 2 for quit |
    while running:
        while start_menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        chosen += 1
                        if chosen == 3:
                            chosen = 0
                    if event.key == pygame.K_UP:
                        chosen -= 1
                        if chosen == -1:
                            chosen = 2

                    if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                        # start game
                        if chosen == 0:
                            game_loop = True
                            start_menu = False
                        # go to settings
                        if chosen == 1:
                            settings_menu = True
                            start_menu = False
                        if chosen == 2:
                            # quit game
                            running = False

            screen = pygame.display.set_mode((create.width, create.height))
            Background_ = create.create_backgound(screen)

            # title
            pygame.font.init()
            font = pygame.font.SysFont("arialblack", 40)
            TEXT_COL = (50, 50, 50)
            TEXT = font.render("WELCOME TO SNAKE", True, TEXT_COL)
            rect = TEXT.get_rect()
            rect.update(110.5, 20, TEXT.get_size()[0], TEXT.get_size()[1])
            screen.blit(TEXT, (110.5, 20))

            # QUIT_BUTTON, buttons = classes.Button()
            PLAY_BUTTON, SETTINGS_BUTTON, QUIT_BUTTON, buttons = create.create_buttons((rect.x, rect.y))

            PLAY_BUTTON.update(screen, chosen == 0)
            SETTINGS_BUTTON.update(screen, chosen == 1)
            QUIT_BUTTON.update(screen, chosen == 2)

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

        chosen = 0  # | 0 for difficulty | 1 for size | 2 for return |
        scroll = 1
        pygame.font.init()
        font = pygame.font.SysFont("arialblack", 40)
        TEXT_COL = (50, 50, 50)
        TEXT = font.render("SETTINGS", True, TEXT_COL)
        x = (width - TEXT.get_size()[0]) / 2
        y = 20
        rect = TEXT.get_rect()
        DIFFICULTY_BUTTON, SIZE_BUTTON, difficulty_slider, RETURN_BUTTON = create.create_settings((x, y))
        diff_s = False
        while settings_menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN or (event.type == pygame.K_RIGHT and diff_s):
                    if not diff_s:
                        if event.key == pygame.K_DOWN:
                            chosen += 1
                            if chosen >= 3:
                                chosen = 0
                    if diff_s:
                        scroll += 1
                        if scroll == 4:
                            scroll = 0
                    if event.key == pygame.K_UP or (event.type == pygame.K_LEFT and diff_s):
                        if not diff_s:
                            chosen -= 1
                            if chosen <= -1:
                                chosen = 3
                        if diff_s:
                            scroll -= 1
                            if scroll == 0:
                                scroll = 4

                    if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                        if not diff_s:
                            # start game
                            if chosen == 0:
                                diff_s = True
                            else:
                                diff_s = False
                            # go to settings
                            if chosen == 1:
                                settings_menu = True
                                start_menu = False
                            if chosen == 2:
                                # return to mine menu
                                start_menu = True
                                settings_menu = False
                        if diff_s:
                            if scroll == 1:
                                fps = 0
                            if scroll == 2:
                                fps = 10
                            if scroll == 3:
                                fps = 15
                            if scroll == 4:
                                fps = 20


            screen = pygame.display.set_mode((create.width, create.height))
            Background_ = create.create_backgound(screen)

            # title
            rect.update(x, y, TEXT.get_size()[0], TEXT.get_size()[1])
            screen.blit(TEXT, (x, y))

            # buttons
            if diff_s:
                DIFFICULTY_BUTTON.update(screen, True)
                if scroll != 2:
                    difficulty_slider[scroll].update(screen, True)
                else:
                    difficulty_slider[scroll].update(screen, False)

            if not diff_s:
                DIFFICULTY_BUTTON.update(screen, chosen == 0)
                SIZE_BUTTON.update(screen, chosen == 1)
            RETURN_BUTTON.update(screen, chosen == 2)

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
