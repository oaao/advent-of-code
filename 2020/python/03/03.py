"""
EXERCISE PROMPT: http://adventofcode.com/2020/day/3
"""
from __future__ import annotations
from typing import List, Dict, Tuple

import operator

INPUT = [
	list(c.strip('\n'))
	for c in open('input', mode='r', encoding='utf-8')
]


class Matrix2D:

	def __init__(self, contents=List[List]) -> None:

		self.contents = contents
		self.x_bound  = len(contents[0])
		self.y_bound  = len(contents)
	
	def __getitem__(self, coord: Tuple[int, int]):

		x, y = coord

		return self.contents[y][x]


def travel_slope(
	pattern: List[List[str]],
	slope:   Tuple[int, int],
	origin:  Tuple[int, int] = (0,0)
) -> List[Dict[tuple, str]]:

	pattern   = Matrix2D(pattern)
	slope     = slope[0], -slope[1]

	current   = tuple(map(operator.add, origin, slope))
	slope_seq = {current: pattern[current], }

	while current[1] < pattern.y_bound - 1:

		x, y    = tuple(map(operator.add, current, slope))
		current = (x % pattern.x_bound, y)
		slope_seq[current] = pattern[current]

	return slope_seq


# part A solution
print(
	list(
		travel_slope(INPUT, slope=(3,-1), origin=(0,0)).values()
	).count('#')
)

