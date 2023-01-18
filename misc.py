import classes

def get_color(n):
    # the color of the fruit
    if n.type == classes.Spots.FRUIT:
        return (243, 11, 28)
    # the color of the snake
    if n.type == classes.Spots.HEAD:
        return (138, 43, 226)

    if n.type == classes.Spots.BODY:
        return (187, 54, 105)

    if n.type == classes.Spots.TAIL:
        return (252, 42, 232)


def get_dir(slots_s, c, snakes):
    for n in range(len(slots_s)):
        l = slots_s[n]
        if c.index == 939:
            c = snakes[len(snakes)-2]
        if c.dir == classes.Dir.UP:
            if l.line == c.line - 1 and l.row == c.row:
                return l
        if c.dir == classes.Dir.DOWN:
            if l.line == c.line + 1 and l.row == c.row:
                return l
        if c.dir == classes.Dir.RIGHT:
            if l.row == c.row + 1 and l.line == c.line:
                return l
        if c.dir == classes.Dir.LEFT:
            if l.row == c.row - 1 and l.line == c.line:
                return l


def get_center(rect, sprite):
    x = sprite.x + (sprite.size[0]) / 2
    x = int(x)
    y = sprite.y + (sprite.size[1]) / 2
    y = int(y)
    rect.center = (x, y)
    return rect


def longer(snakes, size, g, screen):
    f = 41
    snake = classes.snake(snakes, size, g, f)
    t = snakes[0].x
    g = snakes[0].y
    distens = 15
    if snake.dir == classes.Dir.RIGHT:
        snakes[0].x = snakes[0].x - distens
        snakes[0].y = snakes[0].y
    if snake.dir == classes.Dir.LEFT:      
        snakes[0].x = snakes[0].x + distens
        snakes[0].y = snakes[0].y
    if snake.dir == classes.Dir.UP:
        snakes[0].x = snakes[0].x   
        snakes[0].y += 135
    if snake.dir == classes.Dir.DOWN:
        snakes[0].x = snakes[0].x
        snakes[0].y = snakes[0].y - distens
    print(snake.type)
    snake.x = t
    snake.y = g
    snake.index = 0
    snake.rect.update(snake.x, snake.y, size[0], size[1])
    screen.blit(snake.image, (snake.x, snake.y))
    snakes[0].rect.update(snakes[0].x, snakes[0].y, size[0], size[1])
    screen.blit(snakes[0].image, (snakes[0].x, snakes[0].y))
    snake.new = False
    snakes.insert(1, snake)
    snakes.append(snake)
    snakes[1].index = 1
    snakes[0].index = 0
    snakes[1].type = classes.Spots.BODY
    snakes[1].color = get_color(snakes[1])
    return snakes
