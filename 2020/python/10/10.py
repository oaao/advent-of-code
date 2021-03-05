"""
EXERCISE PROMPT: http://adventofcode.com/2020/day/10
"""
from typing import Dict, List

from functools import lru_cache


INPUT = [int(n.strip('\n'))	for n in open('input', mode='r', encoding='utf-8')]


def get_joltage_differences(ratings: List[int]) -> Dict[int, int]:

	difference_counter = {
		1: 0,
		2: 0,
		3: 0
	}

	nums = [0] + sorted(ratings) + [max(ratings) + 3]
	seq  = list(zip(nums, nums[1:]))

	for a, b in seq:
		difference_counter[b - a] += 1

	return difference_counter

# part A solution:
dc = get_joltage_differences(INPUT)
print(dc[1] * dc[3])
