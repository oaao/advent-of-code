"""
EXERCISE PROMPT: http://adventofcode.com/2016/day/2
"""

INPUT = [[int(s) for s in x.split()] for x in open('input.txt')]           # rows turned into lists of int sizes


def validate(side_trios):
    return [filter(lambda x: sum(x) > max(x) * 2, side_trios)]             # no need to sort or over-complicate


def to_cols(side_trios):                                                   # construct Part B input:
    return [
            [a[x], b[x], c[x]]                                             # columns via traversing indices,
            for a, b, c in [zip(*(iter(side_trios),) * 3)]                 # in each triplet of side trios
            for x in range(3)
            ]

print(len(validate(INPUT)))                                                # output Part A answer
print(len(validate(to_cols(INPUT))))                                       # output Part B answer
