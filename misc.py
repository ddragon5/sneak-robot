import classes

def get_color(n):
    # the color of the fruit
    if n.type == classes.Spots.FRUIT:
        return
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


def longer(snakes, size, g):
    f = 41
    snake = snakes[0]
    print(snakes[0].id)
    if snakes[0].dir == classes.Dir.RIGHT:
        print('efdz')
        snake.x -= 15
    if snakes[0].dir == classes.Dir.LEFT:
        print('efdz')
        snake.x += 15
    if snakes[0].dir == classes.Dir.UP:
        print('efdz')
        snake.y -= 15
    if snakes[0].dir == classes.Dir.DOWN:
        print('efdz')
        snake.y += 15

    snakes[0].type = classes.Spots.BODY
    snake.type = classes.Spots.TAIL
    snakes.reverse()
    snakes.append(snake)
    snakes.reverse()
    snakes[1].index = 1
    snakes[0].index = 0
    print(snake.x, snakes[1].x)
    print(snake.y, snakes[1].y)
    return snakes
