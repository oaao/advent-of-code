"""
EXERCISE PROMPT: http://adventofcode.com/2017/day/3
"""

INPUT = 361527


def walk_spiral(n):

    x, y  = 0, 0                                                           # start at centre of spiral
    x_dir = 0
    y_dir = -1                                                             # our first "turn" takes us (1, 0) direction

    for i in range(1, n):                                                  # first "number" on grid is 1, not 0
        if (x == y) or (x > 0 and x == 1 - y) or (x < 0 and x == -y):      # conditions for CCW turn
            x_dir, y_dir = -y_dir, x_dir
        x, y = x + x_dir, y + y_dir                                        # continue in given direction

    return x, y

print(sum(abs(n) for n in walk_spiral(INPUT)))                             # Part A solution
