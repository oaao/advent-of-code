"""
EXERCISE PROMPT: http://adventofcode.com/2021/day/8
"""


INPUT = [
	[
		sorted(sorted(pattern.split(' ')), key=len),
		sorted(output.split(' '))
	]
	for (pattern, output) in
	(line.strip('\n').split(' | ') for line in open('_input', mode='r', encoding='utf-8'))
]

# HELPERS / STATICS -----------------------------------------------------------

def flatten_nested(iterable):
	return sum(iterable, type(iterable)())

DIGITS_HAVING_SEGMENT = {
	'a': (0, 2, 3, 5, 6, 7, 8, 9,),
	'b': (0, 4, 5, 6, 8, 9,),
	'c': (0, 1, 2, 3, 4, 7, 8, 9,),
	'd': (2, 3, 4, 5, 6, 8, 9,),
	'e': (0, 2, 6, 8,),
	'f': (0, 1, 3, 4, 5, 6, 7, 8, 9,),
	'g': (0, 2, 3, 5, 6, 8, 9,),
}

SEGMENT_COUNTS_FOR_DIGITS = {
	digit: flatten_nested(
		tuple(DIGITS_HAVING_SEGMENT.values())
	).count(digit)
	for digit in range(0, 10)
}

DIGIT_FOR_SEGMENT_COUNTS = {v: k for k, v in SEGMENT_COUNTS_FOR_DIGITS.items()}

# SOLUTIONS -------------------------------------------------------------------


def decode_mappings(pattern_output_pairings):
	for pattern, output in pattern_output_pairings:
		matched = dict.fromkeys(SEGMENT_COUNTS_FOR_DIGITS)
		for seq in pattern:
			match len(seq):
				# first, our easy unique lengths:
				case ( 3 | 2 ) as _len:
					print(f'matched seq ---- {seq} to {DIGIT_FOR_SEGMENT_COUNTS[_len]}')
					matched[DIGIT_FOR_SEGMENT_COUNTS[_len]] = seq
					pattern.remove(seq)
				case _:
					print(f"can't match: {seq}")
		print('\n\n', dict(filter(lambda x: x[1], matched.items())), pattern, output)


# part A solution
print(
	sum(
		1 for _ in filter(
			lambda x: len(x) in {SEGMENT_COUNTS_FOR_DIGITS[n] for n in (1, 4, 7, 8)},
			flatten_nested([output for _, output in INPUT])
		)
	)
)


# part B solution:
decode_mappings(INPUT)
print(DIGIT_FOR_SEGMENT_COUNTS)