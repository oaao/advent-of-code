"""
EXERCISE PROMPT: http://adventofcode.com/2020/day/12
"""
from math import cos, sin, radians


INPUT = [
	(
		l[0],
		int(l[1:].strip('\n'))
	) 
	for l in open('input', mode='r', encoding='utf-8')
]


def move(coord, facing, action, val):

	x, y   = coord
	dx, dy = facing

	if action not in {'L', 'R'}:

		_facing = facing

		_coord  = {
			'N': (x,            y + val),
			'S': (x,            y - val),
			'E': (x + val,      y),
			'W': (x - val,      y),
			'F': (x + dx * val, y + dy * val)
		}[action]

	else:

		_coord = coord
		angle  = -val if action == 'R' else val
		rads   = radians(angle % 360)

		_facing = (
			round(dx * cos(rads) - dy * sin(rads)),
			round(dx * sin(rads) + dy * cos(rads))
		)

	#print(f"Doing {action} {val} from {coord}@{facing} to {_coord}@{facing}")
	return _coord, _facing


def navigate(instructions):

	coord  = (0, 0)
	facing = (1, 0) # starts facing east

	for action, val in instructions:
		coord, facing = move(coord, facing, action, val)

	return coord


# part A solution
print(sum(
		map(lambda x: abs(x), navigate(INPUT))
))
