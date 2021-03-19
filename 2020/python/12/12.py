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


def rotate(x, y, angle):

	rads = radians(angle % 360)
	return (
		round(x * cos(rads) - y * sin(rads)),
		round(x * sin(rads) + y * cos(rads))
	)


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

		_facing = rotate(dx, dy, angle)

	#print(f"Doing {action} {val} from {coord}@{facing} to {_coord}@{facing}")
	return _coord, _facing


def navigate(instructions):

	coord  = (0, 0)
	facing = (1, 0) # starts facing east

	for action, val in instructions:
		coord, facing = move(coord, facing, action, val)

	return coord


def move_wp(coord, wp, action, val):

	x, y   = coord
	wx, wy = wp

	if action not in {'L', 'R', 'F'}:

		_coord = coord
		_wp    = {
			'N': (wx,            wy + val),
			'S': (wx,            wy - val),
			'E': (wx + val,      wy),
			'W': (wx - val,      wy),
		}[action]

	elif action == 'F':

		_coord = (x + wx * val, y + wy * val)
		_wp    = wp

	else:

		_coord = coord
		angle  = -val if action == 'R' else val

		_wp = rotate(wx, wy, angle)

	print(f"Doing {action} {val} from {coord}@{wp} to {_coord}@{_wp}")
	return _coord, _wp


def navigate_wp(instructions):

	coord  = (0,  0)
	wp     = (10, 1) # starts 10E 1N of ship

	for action, val in instructions:
		coord, wp = move_wp(coord, wp, action, val)

	return coord


# part A solution
print(sum(
		map(lambda x: abs(x), navigate(INPUT))
))

# part B solution
print(sum(
		map(lambda x: abs(x), navigate_wp(INPUT))
))