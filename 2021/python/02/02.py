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


# part A
def sums_by_key(keys, pairwise_seq):
    d = dict.fromkeys(keys, 0)
    for k, v in pairwise_seq:
        d[k] += v
    return d


d = sums_by_key({"forward", "down", "up"}, INPUT)


# part B
d_aim = dict.fromkeys({"aim", "forward", "depth"}, 0)
for term, n in INPUT:
    match term:
        case "down":
            d_aim["aim"] += n
        case "up":
            d_aim["aim"] -= n
        case "forward":
            d_aim["forward"] += n
            d_aim["depth"] += d_aim["aim"] * n


# part A solution
print(
    operator.mul(
        d["forward"],
        d["down"] - d["up"]
    )
)

# part B solution
print(
    operator.mul(
        d_aim["forward"],
        d_aim["depth"]
    )
)
