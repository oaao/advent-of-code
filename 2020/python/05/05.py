"""
EXERCISE PROMPT: http://adventofcode.com/2020/day/5
"""

from typing import List, Tuple


INPUT = [
	line.translate(line.strip('\n').maketrans('FBLR', '0101'))
	for line in open('input', mode='r', encoding='utf-8')
]


ids = set(int(l, 2) for l in INPUT)


# part A solution
print(max(ids))

# part B solution
print(
	set(
		range(max(ids), min(ids), -1)
	).difference(
		ids
	).pop()
)
