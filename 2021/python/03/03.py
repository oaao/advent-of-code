"""
EXERCISE PROMPT: http://adventofcode.com/2021/day/3
"""
import operator
from itertools import tee


INPUT = [list(map(int, s.strip('\n'))) for s in open('input', mode='r', encoding='utf-8')]


def commonest_per_pos(matrix):
	_len = len(matrix)                #  inv matrix element count; only calc once
	return map(
		round,                        #  nearest-int round -> commonest
		map(
			lambda n: sum(n) / _len,  #  weigh sum vs. _len, since 0..1
			zip(*matrix)              #  simple matrix inversion
		)
	)


def counterpart_bindigit_pair(bindigits):
	a, b = tee(bindigits)
	return (
		a, 
		map(lambda x: int(operator.__not__(x)), b)  # int-as-bool inversion
	)


def bindigits_to_int(digits_iter):
	return int(''.join(map(str, digits_iter)), 2)


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
