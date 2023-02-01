import classes
import pygame
import os

def get_color(n, skin=0):
    # the color of the fruit
    color = ';lksjcvbglgjhckvb'
    if n.type == classes.Spots.FRUIT:
        return (243, 11, 28)
    # the color of the snake
    t = 1, 2, 3
    if n.type.value in t:
        if skin == 0:
            return (236, 190, 2)

        if skin == 1:
            return (39, 79, 113)  # dark blue
        if skin == 2:
            return (111, 28, 240)  # pink
        if skin == 3:
            return (251, 179, 198)  # purple


def get_dir(slots_s, c, snakes):
    for n in range(len(slots_s)):
        l = slots_s[n]
        if c.index == 939:
            c = snakes[len(snakes) - 2]
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


def longer(snakes, size, g, screen, skin):
    f = 41
    snake = classes.snake(snakes, size, g, f, skin)
    t = snakes[0].x
    g = snakes[0].y
    distens = 15
    if snake.dir == classes.Dir.RIGHT:
        snakes[0].x -= distens
        snakes[0].y = snakes[0].y
    if snake.dir == classes.Dir.LEFT:
        snakes[0].x += distens
        snakes[0].y = snakes[0].y
    if snake.dir == classes.Dir.UP:
        snakes[0].x = snakes[0].x
        snakes[0].y -= distens
    if snake.dir == classes.Dir.DOWN:
        snakes[0].x = snakes[0].x
        snakes[0].y += distens

    snake.type = classes.Spots.BODY
    snake.color = get_color(snakes[1])
    snake.x = t
    snake.y = g

    snake.index = 1

    snake.rect.update(snake.x, snake.y, size[0], size[1])
    screen.blit(snake.image, (snake.x, snake.y))

    snakes[0].rect.update(snakes[0].x, snakes[0].y, size[0], size[1])
    screen.blit(snakes[0].image, (snakes[0].x, snakes[0].y))

    snake.new = False
    snakes.insert(1, snake)
    return snakes


########################################################################################################################


def text_box_update(text_box, screen, cords, i, name):
    if len(name) == 0:
        print(type(name))
