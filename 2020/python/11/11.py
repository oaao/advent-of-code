"""
EXERCISE PROMPT: http://adventofcode.com/2020/day/11
"""

from collections import Counter
from copy import deepcopy
import functools

INPUT = [
			[row for row in col]
			for col in [l.strip('\n') for l in open('input', mode='r', encoding='utf-8')]
		]

"""
.: floor
 L: empty
 #: occupied

- if a seat is    empty and there are no occupied seats adjacent to it, the seat is occupied
- if a seat is occupied and four or more seats adjacent to it are also occupied, the seat empties
"""


def show(matrix):
	for row in matrix:
		print(row)


def get_neighbour_counts(row, col, matrix):

	counts = Counter([
		matrix[x][y] for y in range(col-1, col+2)
		if 0 <= y < len(matrix[0])

		for x in range(row-1, row+2)
		if 0 <= x < len(matrix)
	])

	counts[matrix[row][col]] -= 1  # self-exclude cell itself
	return counts


def transform_on_cell(row, col, matrix):

	counts = get_neighbour_counts(row, col, matrix)
	cell   = matrix[row][col]

	if cell == 'L' and counts.get('#', 0) == 0:
		return '#'
	elif cell == '#' and counts.get('#') >= 4:
		return 'L'
	else:
		return cell


def mutate_one_generation(before):

	after = deepcopy(before)

	for row in range(len(before)):
		for col in range(len(before[0])):
			cell = before[row][col]
			if cell == '.':
				after[row][col] == cell
			else:
				after[row][col] = transform_on_cell(row, col, before)

	return after



def mutate_until_stasis(before, counter=[]):

	print(f'iteration {len(counter)}')
	after = mutate_one_generation(before)

	if after == before:
		print('achieved STASIS baby')
		show(after)
		return after
	else:
		show(after)
		print('no match. agane!\n')
		counter.append('')
		return mutate_until_stasis(after)

	return mutate_until_stasis(before)


# part A solution
print(
	[col for row in mutate_until_stasis(INPUT) for col in row].count('#')
)
