"""
EXERCISE PROMPT: http://adventofcode.com/2020/day/5
"""

from typing import Tuple

from functools import reduce

INPUT = [
	line.translate(line.strip('\n').maketrans('FBLR', '0101'))
	for line in open('input', mode='r', encoding='utf-8')
]


# part A solution
print(max(int(l, 2) for l in INPUT))

#print(locate_seat('FBFBBFFRLR'))