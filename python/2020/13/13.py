"""
EXERCISE PROMPT: http://adventofcode.com/2020/day/13
"""
from functools import reduce
from math import gcd

t, series = open('input', mode='r', encoding='utf-8')

t = int(t)
series = [int(s) if s != 'x' else s for s in series.split(',')]


def get_earliest_bus(t, series):
	waits = {
		n - (t % n): n for n in series if n != 'x'
	}

	min_wait = min(waits)
	return (min_wait, waits[min_wait])


def get_earliest_consecutive_timestamp(series):

	def lcm(nums):
		return reduce(lambda x, y: x * y // gcd(x, y), nums)

	seq = [(n, delta) for delta, n in enumerate(series) if n != 'x']

	timestamp = 0
	matched   = {seq[0][0],} # first bus "pre-matched" at t=0

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
