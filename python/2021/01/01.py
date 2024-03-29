"""
EXERCISE PROMPT: http://adventofcode.com/2021/day/1
"""

from itertools import pairwise


INPUT = [int(n.strip('\n')) for n in open('input', mode='r', encoding='utf-8')]


# part A solution
print(
	sum(1 for _ in  # disgusting "generator len counter"
		filter(lambda depth: depth[1] > depth[0], pairwise(INPUT))
	)
)

# part B solution
print(
	sum(1 for _ in  # disgusting "generator len counter"
		filter(
			lambda depth_sums: depth_sums[1] > depth_sums[0],
			pairwise(
				(sum((a, b, c)) for (a, _), (b, c) in pairwise(pairwise(INPUT)))
			)
		)
	)
)
