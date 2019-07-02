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

    return [[None] * width] * height


def apply_claim(claim):
    pass

generate_matrix(claims)