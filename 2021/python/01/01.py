"""
EXERCISE PROMPT: http://adventofcode.com/2021/day/1
"""


INPUT = [int(n.strip('\n')) for n in open('input', mode='r', encoding='utf-8')]


# part A solution
print(
	sum(1 for _ in  # disgusting "generator len counter"
		filter(lambda depth: depth[1] > depth[0], zip(INPUT, INPUT[1:]))
	)
)
