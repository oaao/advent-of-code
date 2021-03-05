"""
EXERCISE PROMPT: http://adventofcode.com/2020/day/10
"""
from typing import List

from collections import Counter

INPUT = [int(n.strip('\n'))	for n in open('_input', mode='r', encoding='utf-8')]


def get_diff_sequence(nums: List[int]) -> List[int]:

	nums = [0] + nums + [max(nums) + 3]
	return [b-a for a, b in list(zip(nums, nums[1:]))]


# universal
nums = sorted(INPUT)

# part A solution:
counts = Counter(get_diff_sequence(nums))
print(counts[1] * counts[3])
