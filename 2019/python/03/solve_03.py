"""
EXERCISE PROMPT: http://adventofcode.com/2019/day/3
"""

from collections import Counter
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
    seen = [(0, 0), ]

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


def get_intersections(wires):

    w1, w2        = [set(travel_wire(w)[1:]) for w in wires]
    intersections = w1.intersection(w2)

    return intersections


def _store_steps(wire):

    tracked = {}

    for step, coord in wire:
        if coord not in tracked:
            tracked[coord] = step

    return tracked


def min_intersection_stepsums(wires):

    stepped = [list(enumerate(travel_wire(wire))) for wire in wires]
    w1, w2  = [_store_steps(w) for w in stepped]

    tracked = Counter(w1) + Counter(w2)

    return min(tracked[coord] for coord in get_intersections(wires))


# part A solution
print(f'A: {min((abs(x) + abs(y)) for x, y in get_intersections(INPUT))}')


print(f'B: {min_intersection_stepsums(INPUT)}')