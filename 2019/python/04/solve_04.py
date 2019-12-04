"""
EXERCISE PROMPT: http://adventofcode.com/2019/day/4
"""

import re#appears in the unlikeliest of places

INPUT = tuple(int(n) for n in open('input.txt', mode='r', ).read().split('-'))


def generate_valid_passwords(range_pair):

    _min, _max = range_pair

    # must be six digits, in range of given input
    initial = [n for n in range(100000, 1000000) if _min <= n <= _max]

    # at least two identical adjacent digits
    adjacencies = [n for n in initial if re.search(r'(.)\1', str(n))]

    # digits never sequentially decrease
    sequentially_valid = []

    for n in adjacencies:

        ln = [int(d) for d in str(n)]
        sq = list(filter(lambda x: x[1] - x[0] >= 0, zip(ln, ln[1:])))

        if len(sq) + 1 == len(ln):
            sequentially_valid.append(n)

    return sequentially_valid


def must_have_doubles(passwords):
    return [pw for pw in passwords if any([str(pw).count(i) == 2 for i in str(pw)])]


# part A solution
print(f'A: {len(generate_valid_passwords(INPUT))}')

# part B solution
print(f'B: {len([pw for pw in generate_valid_passwords(INPUT) if any([str(pw).count(i) == 2 for i in str(pw)])])}')
