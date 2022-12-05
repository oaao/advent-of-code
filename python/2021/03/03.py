"""
EXERCISE PROMPT: http://adventofcode.com/2021/day/3
"""
import operator
from itertools import tee


INPUT = [list(map(int, s.strip('\n'))) for s in open('input', mode='r', encoding='utf-8')]


def commonest_per_pos(matrix):
	_len = len(matrix)                #  inv matrix element count; only calc once
	return map(
		lambda x: int(x + 0.5),       #  0..1 int-round -> commonest (round up at 0.5)
		map(
			lambda n: sum(n) / _len,  #  weigh sum vs. _len, since 0..1
			zip(*matrix)              #  simple matrix inversion
		)
	)


def counterpart_bindigit_pair(bindigits):
	a, b = tee(bindigits)
	return (
		a, 
		map(lambda x: (1, 0)[x], b)  # tuple-index inversion
	)


def bindigits_to_int(digits_iter):
	return int(''.join(map(str, digits_iter)), 2)


def prune_by_digit_commonality(matrix, least_common=False):
	prune_cache = matrix[:]
	for i in range(len(matrix[0])):
		if len(prune_cache) > 1:
			filter_digit = list(commonest_per_pos(prune_cache))[i]
			if least_common:
				filter_digit = int(operator.__not__(filter_digit))
			prune_cache = list(filter(lambda n: n[i] == filter_digit, prune_cache))
	pruned, = prune_cache
	return pruned


def digit_commonality_extremes(matrix):
	by_most_common   = prune_by_digit_commonality(matrix)
	by_least_common  = prune_by_digit_commonality(matrix, least_common=True)
	return (by_most_common, by_least_common)


# part A solution
print(
	operator.mul(
		*map(
			bindigits_to_int,
			counterpart_bindigit_pair(
				commonest_per_pos(INPUT)
			)
		)
	)
)

# part B solution
print(
	operator.mul(
		*map(
			bindigits_to_int,
			digit_commonality_extremes(INPUT)
		)
	)
)

