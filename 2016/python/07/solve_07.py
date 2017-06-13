"""
EXERCISE PROMPT: http://adventofcode.com/2016/day/7
"""

import re#eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee


def mk_either(series, condition):
    left, right = [], []
    for x in series:
        right.append(x) if condition(series, x) else left.append(x)
    return left, right


def has_abba(series):
    return (x for x in series for a, b, c, d in list(zip(x, x[1:], x[2:], x[3:])) if a == d and b == c and a != b)

# e.g. 'a[b]c[d]e' can be read from [a, b, c, d, e] depending on element index
INPUT = (re.split(' ', re.sub('([\[\]])', ' ', x.strip('\n'))) for x in open('input.txt'))

# subgroup  ABBA-unwanted (odd indices inside square brackets) and ABBA-wanted (even were outside)
grp_u_w = (mk_either(x, lambda code, seg: code.index(seg) % 2 == 0) for x in INPUT)

#
can_tls = ((u, w) for u, w in grp_u_w if set(has_abba(w)) and not set(has_abba(u)))

print(len(list(can_tls)))                                             # output Part A solution
