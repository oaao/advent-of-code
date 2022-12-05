"""
EXERCISE PROMPT: http://adventofcode.com/2018/day/3
"""
import re#gret, dishonour, shame, dismay

INPUT = [_.strip('\n') for _ in open('input.txt', mode='r', encoding='UTF-8')]

claim_params = ['id', 'x', 'y', 'w', 'h']
claims       = [
    dict(
        zip(
            claim_params,
            map(int, re.split(' @ |,|: |x', claim[1:]))
        )
    )
    for claim in INPUT
]

def generate_matrix(claims):

    # dynamically generate the matrix based on input extents
    width  = max([(claim['x'] + claim['w']) for claim in claims])
    height = max([(claim['y'] + claim['h']) for claim in claims])

    return [[None for _x in range(width)] for _y in range(height)]


def apply_claim(claim, matrix):

    x, y = claim['x'], claim['y']

    for y_pos in range(claim['h']):
        for x_pos in range(claim['w']):

            if matrix[y + y_pos][x + x_pos] == None:
                matrix[y + y_pos][x + x_pos] = claim['id']
            else:
                matrix[y + y_pos][x + x_pos] = 'x'


def occurrences_in_matrix(element, matrix):
    return len([_x for _y in matrix for _x in _y if _x == element])


# part B
def find_full_claim(claims, matrix):

    for claim in claims:

        full_count = claim['w'] * claim['h']
        actual_count = occurrences_in_matrix(claim['id'], matrix)

        if full_count == actual_count:
            return claim['id']

matrix = generate_matrix(claims)

for claim in claims:
    apply_claim(claim, matrix)

print(f'A: {occurrences_in_matrix("x", matrix)}')
print(f'B: {find_full_claim(claims, matrix)}')
