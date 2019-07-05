"""
EXERCISE PROMPT: http://adventofcode.com/2018/day/7
"""

# >importing re

from sys import maxsize

INPUT = [
    (x[1], x[7])
    for x in
    [s.strip('\n').split(' ') for s in open('input.txt')]
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
