"""
EXERCISE PROMPT: http://adventofcode.com/2018/day/4
"""

from itertools import tee
from functools import reduce

INPUT = open('input.txt').read().strip('\n')

RESULT = 'dabCBAcaDA'

def react(polymer):

    traversal = []

    for c in polymer:
        if traversal and c.swapcase() == traversal[-1]:
            traversal.pop()
        else:
            traversal.append(c)

    return ''.join(traversal)


print(f'A: {len(react(INPUT))}')
