"""
EXERCISE PROMPT: http://adventofcode.com/2020/day/11
"""

import sys, os # for stdout toggling

from collections import Counter
from copy import deepcopy


INPUT = [
			[row for row in col]
			for col in [l.strip('\n') for l in open('input', mode='r', encoding='utf-8')]
		]


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

	counts[matrix[row][col]] -= 1  # self-exclude cell
	return counts


def get_directional_neighbour_counts(row, col, matrix):

	directions = {(x, y) for x in {-1, 0, 1} for y in {-1, 0, 1}}
	
	directional_neighbours = [
		[None for y in range(0, 3)]
		for x in range(0, 3)
	]

	directional_neighbours[1][1] = matrix[row][col]

	for x, y in directions:

		iteration = 1
		satisfied_direction = False

		while not satisfied_direction:

			next_row  = row + (x * iteration)
			next_col  = col + (y * iteration)

			if 0 <= next_row < len(matrix) and 0 <= next_col < len(matrix[0]):

				next_cell = matrix[next_row][next_col]

				if next_cell == '.':
					iteration += 1
				else:
					# (1, 1) is our reference cell for pretend neighbours
					directional_neighbours[1+x][1+y] = next_cell
					satisfied_direction = True
			else:
				# hitting a matrix boundary negates caring about cell value
				satisfied_direction = True

	return get_neighbour_counts(1, 1, directional_neighbours)


def determine_cell_by_neighbours(row, col, matrix, method):

	methods = {
		'adjacent': {
			'function': get_neighbour_counts,
			'max_neighbours': 4
		},
		'directional': {
			'function': get_directional_neighbour_counts,
			'max_neighbours': 5
		}
	}
	max_neighbours = methods[method]['max_neighbours']

	counts = methods[method]['function'](row, col, matrix)
	cell   = matrix[row][col]

	if cell == 'L' and counts.get('#', 0) == 0:
		return '#'
	elif cell == '#' and counts.get('#') >= max_neighbours:
		return 'L'
	else:
		return cell


def mutate_one_generation(before, method):

	after  = deepcopy(before)

	for row in range(len(before)):
		for col in range(len(before[0])):
			cell = before[row][col]
			if cell == '.':
				after[row][col] == cell
			else:
				after[row][col] = determine_cell_by_neighbours(row, col, before, method)

	return after


def mutate_until_stasis(before, method=None, iteration=[None,]):

	print(f'iteration {len(iteration)}')
	after = mutate_one_generation(before, method)

	if after == before:
		show(after)
		print('achieved STASIS baby\n')
		return after
	else:
		show(after)
		print('no match. agane!\n')
		iteration.append(None)
		return mutate_until_stasis(after, method, iteration)

	return mutate_until_stasis(before, method, iteration)



# part A solution
print(
	[col for row in mutate_until_stasis(INPUT, method='adjacent') for col in row].count('#')
)

# part B solution
print(
	[col for row in mutate_until_stasis(INPUT, method='directional') for col in row].count('#')
)
