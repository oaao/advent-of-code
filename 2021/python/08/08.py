"""
EXERCISE PROMPT: http://adventofcode.com/2021/day/8
"""


INPUT = [
	[pattern.split(' '), output.split(' ')] for (pattern, output) in
	(line.strip('\n').split(' | ') for line in open('input', mode='r', encoding='utf-8'))
]

DIGITS_USING_SEGMENT = {
	'a': (0, 2, 3, 5, 6, 7, 8, 9,),
	'b': (0, 4, 5, 6, 8, 9,),
	'c': (0, 1, 2, 3, 4, 7, 8, 9,),
	'd': (2, 3, 4, 5, 6, 8, 9,),
	'e': (0, 2, 6, 8,),
	'f': (0, 1, 3, 4, 5, 6, 7, 8, 9,),
	'g': (0, 2, 3, 5, 6, 8, 9,),
}


def flatten_nested(iterable):
	return sum(iterable, type(iterable)())


def segments_per_digit(digit): 
	return flatten_nested(
		tuple(DIGITS_USING_SEGMENT.values())
	).count(digit)


# part A solution
print(
	sum(
		1 for _ in filter(
			lambda x: len(x) in {segments_per_digit(n) for n in (1, 4, 7, 8)},
			flatten_nested([output for _, output in INPUT])
		)
	)
)

