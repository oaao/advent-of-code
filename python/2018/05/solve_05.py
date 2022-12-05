"""
EXERCISE PROMPT: http://adventofcode.com/2018/day/5
"""

import re#peated use of this module is becoming unsettling

from itertools import tee
from functools import reduce
from string import ascii_lowercase


INPUT = open('input.txt').read().strip('\n')

def react(polymer):

    traversal = []

    for c in polymer:
        if traversal and c.swapcase() == traversal[-1]:
            traversal.pop()
        else:
            traversal.append(c)

    return ''.join(traversal)


# part B solution
def generate_omit_reactions(polymer):

    alpha = 'abcdefghijklmnopqrstuvwxyz'

    omittal_polymers = []

    for c in alpha:

        omittal = re.sub(
            '|'.join((c, c.upper())),
            '',
            polymer
        )

        new_polymer = react(omittal)

        omittal_polymers.append((c, new_polymer))

    return omittal_polymers

omittal_cases         = generate_omit_reactions(INPUT)
shortest_omittal_case = sorted(omittal_cases, key=lambda x: len(x[1]))[0]


print(f'A: {len(react(INPUT))}')
print(f'B: {len(shortest_omittal_case[1])}')
