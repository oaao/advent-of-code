"""
EXERCISE PROMPT: http://adventofcode.com/2020/day/3
"""
from __future__ import annotations
from functools import reduce
from typing import Any, List, Dict, Tuple

import operator

INPUT = [
	list(c.strip('\n'))
	for c in open('input', mode='r', encoding='utf-8')
]


def travel_slope(
	pattern: List[List[Any]],
	slope:   Tuple[int, int],
	origin:  Tuple[int, int] = (0,0)
) -> List[Dict[tuple, str]]:

	x_bound, y_bound = len(pattern[0]), len(pattern)

	x, y      = tuple(map(operator.add, origin, slope))
	slope_seq = {(x, y): pattern[y][x], }

	while y < y_bound - 1:

		_x, _y    = tuple(map(operator.add, (x, y), slope))
		x, y = (_x % x_bound, _y)
		slope_seq[x, y] = pattern[y][x]

	return slope_seq


# part A solution
print(list(travel_slope(INPUT, slope=(3,1), origin=(0,0)).values()).count('#'))

# part B solution
print(
	reduce(
		lambda x, y: x*y, 
		[
			list(travel_slope(INPUT, slope=slope, origin=(0,0)).values()).count('#')
			for slope in [(1,1), (3,1), (5,1), (7,1), (1,2)]
		]
	)
)