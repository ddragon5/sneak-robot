from misc import get_dir, get_color
import classes

def move(c, y, snakes, has_m, s, q):
    redo = True
    while redo:
        try:
            if c.type == classes.Spots.HEAD:
                if has_m[0]:
                    g = snakes, has_m
                    redo = False
                    return snakes, has_m, s
                else:
                    y.tag = ('snake', 'head', 1)
                    y.new = True
                    y.color = (138, 43, 226)
                    y.type = classes.Spots.HEAD
                    c.tag = ('snake', 'body', 2)
                    c.type = classes.Spots.BODY
                    snakes[len(snakes) - 1] = y
                    snakes[len(snakes) - 2] = c
                    has_m[0] = True
                    redo = False
                    g = snakes, has_m
                    return snakes, has_m, s, c
            if c.type == classes.Spots.BODY:
                if has_m[2] >= len(snakes) - 2:
                    g = snakes, has_m
                    redo = False
                    return snakes, has_m, s, c
                else:
                    has_m[2] += 1
                    redo = False
                    return snakes, has_m, s, c
            if c.type == classes.Spots.TAIL:
                if has_m[1]:
                    s[c.index].color = (74, 176, 224)
                    g = snakes, has_m
                    redo = False
                    return snakes, has_m, s, c
                else:
                    r = y
                    r.tag = ('snake', 'last', len(snakes))
                    r.new = True
                    r.color = get_color(r)
                    r.type = classes.Spots.TAIL
                    r.dir_s = c.dir_s
                    snakes[0] = r
                    c.tag = ('floor')
                    c.type = classes.Spots.BLANK
                    c.color = get_color(c)

                    has_m[1] = True
                    g = snakes, has_m
                    redo = False
                    return snakes, has_m, s, c
        except AttributeError:
            redo = True
            print('rtegg')
            y = get_dir(s, c)
    print('gtrs')
    return snakes, has_m, s, c
