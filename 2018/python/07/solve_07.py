"""
EXERCISE PROMPT: http://adventofcode.com/2018/day/6
"""

# >importing re

from collections import OrderedDict
from itertools import groupby
from sys import maxsize

INPUT = [
    tuple(
        s
            .replace(' can begin.', '')
            .replace('must be finished before step ', '')
            .replace('Step ', '')
            .strip('\n')
            .split(' ')
    )
    for s in open('input.txt')
]


# cheaty flattening method: see 2018/02 {factors}
steps = set(sum(INPUT, ()))


# part A solution
def get_next_step(steps, orderings):
    return [
        step for step in steps
        if all(subsequent != step for (_, subsequent) in orderings)
    ]

def get_step_sequence(steps, orderings):

    order     = ''

    while steps:

        possible = list(get_next_step(steps, orderings))
        possible.sort()

        s = possible[0]
        order += s

        steps.remove(s)
        orderings = [(a, b) for (a, b) in orderings if a != s]

    return order

print(f'A: {get_step_sequence(steps, INPUT)}')
