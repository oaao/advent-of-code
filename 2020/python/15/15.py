"""
EXERCISE PROMPT: http://adventofcode.com/2020/day/15
"""


INPUT = tuple(int(n) for n in open('input', mode='r', encoding='utf-8').read().split(','))


def generate_seq(initial, turns=0):

	seen = set(initial[:-1])
	seq  = list(initial)

	for i in range(len(initial), turns):

		n = seq[i-1]

		if n not in seen:
			seq.append(0)
			seen.add(n)
		else:
			a, b = [i for i, x in enumerate(seq) if x == n][-2:]
			seq.append(b-a)

	return seq[-1]


# part A solution
print(generate_seq(INPUT, turns=2020))
