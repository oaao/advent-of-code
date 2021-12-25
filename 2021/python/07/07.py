"""
EXERCISE PROMPT: http://adventofcode.com/2021/day/7
"""

INPUT = [int(x) for x in open('input', mode='r', encoding='utf-8').read().strip('\n').split(',')]


def alignment_costs_per_pos(positions):
	return {
		pos: sum(abs(x-pos) for x in positions)
		for pos in positions
	}



# part A solution:
print(
	min(
		alignment_costs_per_pos(INPUT).values()
	)
)
