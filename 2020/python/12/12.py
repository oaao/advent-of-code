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


def move(coord, ref, action, val, mode='direction'):

	x, y   = coord
	dx, dy = ref # either the directional vector or the offset waypoint

	if action not in {'L', 'R', 'F'}:

		tx, ty = ref if mode == 'waypoint' else coord
		_point = {
			'N': (tx,            ty + val),
			'S': (tx,            ty - val),
			'E': (tx + val,      ty),
			'W': (tx - val,      ty),
		}[action]

		if mode == 'waypoint':
			_ref   = _point
			_coord = coord
		else:
			_coord = _point
			_ref   = ref

	if action == 'F':
		_coord = (x + dx * val, y + dy * val)
		_ref   = ref

	elif action in {'L', 'R'}:

		_coord = coord
		angle  = -val if action == 'R' else val

		_ref = rotate(dx, dy, angle)

	#print(f"Doing {action} {val} from {coord}@{ref} to {_coord}@{_ref}")
	return _coord, _ref


def navigate(instructions, mode='direction'):

	coord = (0, 0)
	ref   = (10, 1) if mode == 'waypoint' else (1, 0)

	for action, val in instructions:
		coord, ref = move(coord, ref, action, val, mode)

	return coord


# part A solution
print(sum(
		map(lambda x: abs(x), navigate(INPUT))
))

# part B solution
print(sum(
		map(lambda x: abs(x), navigate(INPUT, mode='waypoint'))
))