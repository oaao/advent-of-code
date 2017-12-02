"""
EXERCISE PROMPT: http://adventofcode.com/2017/day/2
"""

import itertools

INPUT = list([int(x) for x in row.strip('\n').split('\t')] for row in open('input.txt', mode='r', encoding='UTF-8'))

print(sum((max(x) - min(x)) for x in INPUT))                                                                                        # part A solution
print(sum(int((max(a, b) / min(a, b))) for x in INPUT for a, b in itertools.combinations(x, 2) if (max(a, b) % min(a, b) == 0)))    # part B solution
