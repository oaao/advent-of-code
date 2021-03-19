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


def move(coord, rel, action, val, mode='direction'):

	x, y   = coord
	dx, dy = rel    # relative element: directional vector or offset waypoint

	if action not in {'L', 'R', 'F'}:

		tx, ty = rel if mode == 'waypoint' else coord
		_point = {
			'N': (tx,            ty + val),
			'S': (tx,            ty - val),
			'E': (tx + val,      ty),
			'W': (tx - val,      ty),
		}[action]

		if mode == 'waypoint':
			_rel   = _point
			_coord = coord
		else:
			_coord = _point
			_rel   = rel

	if action == 'F':
		_coord = (x + dx * val, y + dy * val)
		_rel   = rel

	elif action in {'L', 'R'}:

		_coord = coord
		angle  = -val if action == 'R' else val
		rads   = radians(angle % 360)

		_rel = (
			round(dx * cos(rads) - dy * sin(rads)),
			round(dx * sin(rads) + dy * cos(rads))
		)

	#print(f"Doing {action} {val} from {coord}@{rel} to {_coord}@{_rel}")
	return _coord, _rel


def navigate(instructions, mode='direction'):

	coord = (0, 0)
	rel   = (10, 1) if mode == 'waypoint' else (1, 0)

	for action, val in instructions:
		coord, rel = move(coord, rel, action, val, mode)

	return coord


# part A solution
print(
	sum(map(abs, navigate(INPUT)))
)

# part B solution
print(
	sum(map(abs, navigate(INPUT, mode='waypoint')))
)
