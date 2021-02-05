"""
EXERCISE PROMPT: http://adventofcode.com/2020/day/6
"""

INPUT = [
	[set(answer) for answer in group.split('\n')]
	for group in open('input', mode='r', encoding='utf-8').read().split('\n\n')
]


def count_affirmatives(data, consensus=False):

	f = set.intersection if consensus else set.union

	return (len(f(*group)) for group in data)


# part A solution
print(
	sum(count_affirmatives(INPUT))
)
