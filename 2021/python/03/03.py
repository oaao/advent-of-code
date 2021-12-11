"""
EXERCISE PROMPT: http://adventofcode.com/2021/day/3
"""
import operator
from itertools import tee


INPUT = [list(map(int, s.strip('\n'))) for s in open('input', mode='r', encoding='utf-8')]


# part A
_len = len(INPUT)                 #  inv matrix element count; only calc once
most_common_digits = map(
	round,                        #  nearest-int round of float sum -> most common
	map(
		lambda n: sum(n) / _len,  #  weigh sum vs. _len, since 0..1
		zip(*INPUT)               #  simple matrix inversion
	)
)

a, b = tee(most_common_digits)
b    = map(lambda x: int(operator.__not__(x)), b)  # int-as-bool shenanigans


# part A solution
print(
	operator.mul(
		int(''.join(map(str, a)), 2),
		int(''.join(map(str, b)), 2)
	)
)
