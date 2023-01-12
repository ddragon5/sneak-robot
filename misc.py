import classes


def get_color(n):
    # the color of the background
    if n.type.value == 0:
        if n.line % 2 != 0:
            if n.row % 2 != 0:
                return (155, 206, 62)  # darker
            else:
                return (170, 215, 81)  # lighter
        else:
            if n.row % 2 == 0:
                return (155, 206, 62)  # darker
            else:
                return (170, 215, 81)  # lighter
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
