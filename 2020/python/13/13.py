"""
EXERCISE PROMPT: http://adventofcode.com/2020/day/13
"""
from functools import reduce
from math import gcd

t, series = open('input', mode='r', encoding='utf-8')

t = int(t)
series = [int(s) if s != 'x' else 0 for s in series.split(',')]


def get_earliest_bus(t, series):
	waits = {
		n - (t % n): n for n in series if n > 0
	}

	min_wait = min(waits)
	return (min_wait, waits[min_wait])


def get_earliest_consecutive_timestamp(series):

	seq   = [(n, delta) for delta, n in enumerate(series) if n > 0]
	first = seq[0][0]

	timestamp = 0
	matched   = {first,}

	def lcm(nums):
		return reduce(lambda x, y: x * y // gcd(x, y), nums)

	while len(matched) < len(seq):

		timestamp += lcm(matched)

		for n, delta in seq:
			if (timestamp + delta) % n == 0:
				matched.add(n)

	return timestamp


# part A solution
wait, route = get_earliest_bus(t, series)
print(wait * route)

# part B
print(get_earliest_consecutive_timestamp(series))
