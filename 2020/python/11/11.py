"""
EXERCISE PROMPT: http://adventofcode.com/2020/day/11
"""

from collections import Counter
from copy import deepcopy
import functools

INPUT = [
			[row for row in col]
			for col in [l.strip('\n') for l in open('_input', mode='r', encoding='utf-8')]
		]


def show(matrix):
	for row in matrix:
		print(row)


def get_adjacent_neighbours(row, col, matrix):

	counts = Counter([
		matrix[x][y] for y in range(col-1, col+2)
		if 0 <= y < len(matrix[0])

		for x in range(row-1, row+2)
		if 0 <= x < len(matrix)
	])

	counts[matrix[row][col]] -= 1  # self-exclude cell itself
	return counts


def determine_cell_by_neighbours(row, col, matrix, method='adjacent'):

	methods = {
		'adjacent': {
			'function': get_adjacent_neighbours,
			'max_neighbours': 4
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


def mutate_until_stasis(before, counter=[], method='adjacent'):

	print(f'iteration {len(counter)}')
	after = mutate_one_generation(before, method)

	if after == before:
		show(after)
		print('achieved STASIS baby\n')
		return after
	else:
		show(after)
		print('no match. agane!\n')
		counter.append(None)
		return mutate_until_stasis(after, counter, method)

	return mutate_until_stasis(before, counter, method)


# easy print() toggle, because the stdout is fun for this one
# import sys, os; sys.stdout = open(os.devnull, 'w')
	
# part A solution
print(
	[col for row in mutate_until_stasis(INPUT) for col in row].count('#')
)
