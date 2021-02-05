"""
EXERCISE PROMPT: http://adventofcode.com/2020/day/6
"""

INPUT = [
	group.split('\n')
	for group in open('input', mode='r', encoding='utf-8').read().split('\n\n')
]


# part A solution
print(
	sum(
		len(set(''.join(group)))
	for group in INPUT)
)
