"""
EXERCISE PROMPT: http://adventofcode.com/2020/day/15
"""


INPUT = tuple(int(n) for n in open('input', mode='r', encoding='utf-8').read().split(','))


def generate_seq(initial, turns=0):

	seen = {n: i+1 for i, n in enumerate(initial)}
	n    = initial[-1] 

	for i in range(len(initial), turns):
		seen[n], n = i, i - seen.get(n, i)

	return n


# part A solution
print(generate_seq(INPUT, turns=2020))

# part B
print(generate_seq(INPUT, turns=30000000))
