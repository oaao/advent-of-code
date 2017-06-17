"""
EXERCISE PROMPT: http://adventofcode.com/2016/day/7
"""

# NOTE: Choosing to solve this exercise in a manner which preserves IP data, rather than simply arrives at the answer.

import re#eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee


def mk_either(series, condition):
    left, right = [], []
    for el in series:
        right.append(el) if condition(series, el) else left.append(el)
    return left, right


def has_abba(series):
    return (_ for _ in series for a, b, c, d in zip(_, _[1:], _[2:], _[3:]) if a == d and b == c and a != b)


def has_aba(series):
    return ((a, b, c) for _ in series for a, b, c in zip(_, _[1:], _[2:]) if a == c and a != b)


def rmk_ips(ips):

    # N.B. We have been using (hn, sn) as Left, Right; actual IP starts with sn so order is reversed in zipping.
    flattened = ([c for c_pair in list(zip(sn, hn + [''])) for c in c_pair] for hn, sn in ips)
    bracketed = (zip(c, (brkt for i in range(len(list(c))) for brkt in ('[', ']'))) for c in flattened)

    # We slice off the last element of the list, because it will be an unneeded trailing '['
    return ("".join([c_subel for c_el in list(c_list)[:-1] for c_subel in c_el][:-1]) for c_list in bracketed)

# e.g. 'a[b]c[d]e' can be read from [a, b, c, d, e] depending on element index
INPUT = (re.split(' ', re.sub('([\[\]])', ' ', _.strip('\n'))) for _ in open('input.txt'))

# subgroup  ABBA-unwanted (odd indices inside square brackets) and ABBA-wanted (even were outside)
grp_h_s = [mk_either(ip, lambda code, seg: code.index(seg) % 2 == 0) for ip in INPUT]

# an empty element, e.g. [], evaluates False, therefore:
can_tls = set(rmk_ips((hn, sn) for hn, sn in grp_h_s if set(has_abba(sn)) and not set(has_abba(hn))))
can_ssl = set(rmk_ips((hn, sn) for hn, sn in grp_h_s for a, b, c in set(has_aba(hn)) if (b, a, b) in set(has_aba(sn))))

print(len(can_tls))                                           # output Part A solution
print(len(can_ssl))                                           # output Part B solution
