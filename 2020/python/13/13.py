"""
EXERCISE PROMPT: http://adventofcode.com/2020/day/13
"""

t, series = open('input', mode='r', encoding='utf-8')

t = int(t)
series = [int(s) for s in series.split(',') if s != 'x']


def get_earliest_bus(t, series):
	waits = {
		n - (t % n): n
		for n in series
	}

	min_wait = min(waits)
	return (min_wait, waits[min_wait])


# part A solution
wait, route = get_earliest_bus(t, series)
print(wait * route)