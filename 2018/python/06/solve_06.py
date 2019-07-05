"""
EXERCISE PROMPT: http://adventofcode.com/2018/day/6
"""

from collections import Counter

INPUT = [
    tuple(
        map(
            int,
            x.strip('\n').split(', ')
        )
    )
    for x in open('input.txt').readlines()
]

decoupled  = list(zip(*INPUT))
max_x, max_y       = max(decoupled[0]), max(decoupled[1])

def get_hydrated_matrix(coords):

    matrix = {}

    for _x in range(max_x):
        for _y in range(max_y):

            man_min = min(
                abs(_x - coord_x) + abs(_y - coord_y)
                for coord_x, coord_y in coords
            )

            for i, (coord_x, coord_y) in enumerate(coords):
                if abs(_x - coord_x) + abs(_y - coord_y) == man_min:
                    if matrix.get((_x, _y), -1) != -1:
                        matrix[_x, _y] = -1
                        break
                    matrix[_x, _y] = i

    return matrix

# part A solution
matrix = get_hydrated_matrix(INPUT)

non_infinite_areas = set([-1]) \
    .union(set(matrix[x, max_y - 1] for x in range(max_x))) \
    .union(set(matrix[x,         0] for x in range(max_x))) \
    .union(set(matrix[max_x - 1, y] for y in range(max_y))) \
    .union(set(matrix[0,         y] for y in range(max_y)))

largest_non_infinite_area = next(
    i[1] for i in Counter(matrix.values()).most_common()
    if i[0] not in non_infinite_areas
)


print(f'A: {largest_non_infinite_area}')
