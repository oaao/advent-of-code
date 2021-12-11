"""
EXERCISE PROMPT: http://adventofcode.com/2021/day/2
"""
import operator


INPUT = list(
    map(
        lambda x: (x[0], int(x[1])),
        map(
            lambda s: s.strip('\n').split(' '),
            open('input', mode='r', encoding='utf-8')
        )
    ),
)


def sums_by_key(keys, pairwise_seq):
    d = dict.fromkeys(keys, 0)
    for k, v in pairwise_seq:
        d[k] += v
    return d

d = sums_by_key({"forward", "down", "up"}, INPUT)


# part A solution
print(
    operator.mul(
        d["forward"],
        d["down"] - d["up"]
    )
)
