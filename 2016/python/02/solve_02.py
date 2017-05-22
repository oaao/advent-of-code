"""
EXERCISE PROMPT: http://adventofcode.com/2016/day/2
"""

INPUT = list(x.strip('\n') for x in open('input.txt'))             # get rid of newline; it is not a valid "move"

keypad = {
    (-1, 1):  1,
    (0, 1):   2,
    (1, 1):   3,
    (-1, 0):  4,
    (0, 0):   5,
    (1, 0):   6,
    (-1, -1): 7,
    (0, -1):  8,
    (1, -1):  9
}

instr = {
    'U':  (0, 1),
    'D':  (0, -1),
    'R':  (1, 0),
    'L':  (-1, 0)
}


def bound(x, mi, ma):                                              # disallow movement beyond keypad edges
    return max(min(x, ma), mi)


def kp_nav(moves, start):

    coord = start

    for m in moves:
        unbound = (ta + tb for ta, tb in zip(coord, instr[m]))
        coord   = tuple(bound(x, -1, 1) for x in unbound)

    return coord

code = [keypad[kp_nav(m, (0, 0))] for m in INPUT]                  # look up keypad number for each instruction line

print(''.join(map(str, code)))                                     # output Part A solution
