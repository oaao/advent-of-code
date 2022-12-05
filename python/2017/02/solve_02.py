"""
EXERCISE PROMPT: http://adventofcode.com/2017/day/2
"""

import itertools

INPUT = list([int(x) for x in row.strip('\n').split('\t')] for row in open('input.txt', mode='r', encoding='UTF-8'))

print(sum(b - a for a, *middle, b in map(sorted, INPUT)))                                               # part A solution
print(sum(b // a for row in INPUT for a, b in itertools.combinations(sorted(row), 2) if b % a == 0))    # part B solution