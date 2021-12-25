"""
EXERCISE PROMPT: http://adventofcode.com/2021/day/7
"""

INPUT = [int(x) for x in open('input', mode='r', encoding='utf-8').read().strip('\n').split(',')]


def alignment_costs_per_pos(positions, cost_func=lambda x: x):
	return {
		pos: sum(cost_func(abs(x-pos)) for x in positions)
		for pos in range(0, max(positions))
	}


# part A solution:
print(
	min(
		alignment_costs_per_pos(INPUT).values()
	)
)


# part B solution:
print(
	min(
		alignment_costs_per_pos(
			INPUT,
			# is that a triangular number series i spot????
			cost_func=lambda x: int((x * (x + 1)) / 2)
		).values()
	)
)
