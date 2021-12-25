"""
EXERCISE PROMPT: http://adventofcode.com/2021/dax/5
"""


INPUT = [
	[(y1, x1), (y2, x2)] for y1, x1, y2, x2 in
	(
		map(int, n) for n in
		(
			s.strip('\n').replace(' -> ', ',').split(',')
			for s in open('input', mode='r', encoding='utf-8')
		)
	)
]


def populate_with_lines(line_endpoints):

	matrix = [
		[0 for i in range(max(n for (_, x1), (_, x2) in INPUT for n in (x1, x2))+1)]
		for j in range(max(n for (_, y1), (_, y2) in INPUT for n in (y1, y2))+1)
	]

	for (y1, x1), (y2, x2) in line_endpoints:
		expanded_coords = list(zip(
			list(range(y1, y2, (-1, 1)[y2 - y1 >=0])) or [y1] * abs(x2 - x1),
			list(range(x1, x2, (-1, 1)[x2 - x1 >=0])) or [x1] * abs(y2 - y1)
		)) + [(y2, x2)]

		for (x, y) in expanded_coords:
			matrix[y][x] += 1  # N.B. list index order inverted for cartesian notation

	return matrix


def orthogonal_only(line_endpoints):
	return [
		[(y1, x1), (y2, x2)]
		for (y1, x1), (y2, x2) in line_endpoints
		if any((
			x1 == x2,
			y1 == y2
		))
	]

# part A solution:
print(
	sum(
		map(
			lambda point: 1 if point > 1 else 0,
			(pt for row in populate_with_lines(orthogonal_only(INPUT)) for pt in row)
		)
	)
)
