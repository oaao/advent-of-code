"""
EXERCISE PROMPT: http://adventofcode.com/2019/day/3
"""

from itertools import chain

INPUT = [
    [
        (i[0], int(i[1:]))
        for i in wire.split(',')
    ]

    for wire in open('input.txt', mode='r', ).read().rstrip().splitlines()
]


def travel_wire(wire):

    x, y = 0, 0
    seen = []

    for d, n in wire:

        # if-check should be more efficient than function call w/ switch-case
        if   d == 'U':
            seen.extend((x, y + c) for c in range(1, n+1))
            y += n
        elif d == 'D':
            seen.extend((x, y - c) for c in range(1, n+1))
            y -= n
        elif d == 'R':
            seen.extend((x + c, y) for c in range(1, n+1))
            x += n
        elif d == 'L':
            seen.extend((x - c, y) for c in range(1, n+1))
            x -= n

    return seen


def closest_intersection_mhd(wires):

    w1, w2        = [set(travel_wire(w)) for w in INPUT]
    intersections = w1.intersection(w2)

    return min((abs(x) + abs(y)) for x,y in intersections)


# part A solution
print(f'A: {closest_intersection_mhd(INPUT)}')


