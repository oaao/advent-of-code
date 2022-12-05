"""
EXERCISE PROMPT: http://adventofcode.com/2020/day/9
"""
from typing import List, Tuple


INPUT = [int(n.strip('\n'))	for n in open('input', mode='r', encoding='utf-8')]



def get_first_invalid_enum(nums: List[int], interval: int=25) -> Tuple[int, int]:
	
	index = interval
	
	for i, n in enumerate(nums[index:]):

		check_span = nums[index-interval:index]

		if any((n-x in check_span for x in check_span)):
			index += 1
		else:
			return (i, n)
			break


def sum_contiguous_addend_extremes(nums: List[int], interval: int=25) -> int:
	"""fuck it let's grind the shit out of some sublists"""

	i, n = get_first_invalid_enum(nums, interval)

	for a in range(0, i):
		for b in range(a, i):

			check_span = nums[a:b]

			if sum(check_span) == n:
				return min(check_span) + max(check_span)


# part A solution
print(get_first_invalid_enum(INPUT)[1])

# part B solution
print(sum_contiguous_addend_extremes(INPUT))
