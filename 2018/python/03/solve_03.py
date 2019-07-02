"""
EXERCISE PROMPT: http://adventofcode.com/2018/day/3
"""
import re#gret, dishonour, shame, dismay

INPUT = [_.strip('\n') for _ in open('input.txt', mode='r', encoding='UTF-8')]

# [claim_id, from_left, from_top, w, h]
claims = [list(map(int, re.split(' @ |,|: |x', claim[1:]))) for claim in INPUT]

def generate_matrix(claims):

    # dynamically generate the matrix based on input extents
    width  = max([(from_left + w) for claim_id, from_left, from_top, w, h in claims])
    height = max([(from_top  + h) for claim_id, from_left, from_top, w, h in claims])

    return [[None for _x in range(width)] for _y in range(height)]


def apply_claim(claim, matrix):

    claim_id, x, y, width, height = claim[0], claim[1], claim[2], claim[3], claim[4]

    for y_pos in range(height):
        for x_pos in range(width):

            #import pdb; pdb.set_trace()

            if matrix[y + y_pos][x + x_pos] == None:
                matrix[y + y_pos][x + x_pos] = claim_id
            else:
                matrix[y + y_pos][x + x_pos] = 'x'

matrix = generate_matrix(claims)

for claim in claims:
    apply_claim(claim, matrix)

print(f'A: {len([x for y in matrix for x in y if x == "x"])}')
