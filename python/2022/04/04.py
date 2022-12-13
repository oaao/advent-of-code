"""
EXERCISE PROMPT: http://adventofcode.com/2022/day/4
"""
import itertools

INPUT = tuple(
    tuple(
        tuple(map(int, section.split("-")))
        for section in line.split(",")
    )
    for line in open("input", "r", encoding="utf-8").read().strip().split("\n")
)

# part A solution
print(
    sum(
        any(
            a1 >= b1 and a2 <= b2
            for ((a1, a2), (b1, b2)) in itertools.permutations(sorted(line))
        )
        for line in INPUT
    )
)

# part B solution
print(
    sum(
        any(
            set(range(a1, a2 + 1)).intersection(set(range(b1, b2 + 1)))
            for ((a1, a2), (b1, b2)) in itertools.combinations(sorted(line), 2)
        )
        for line in INPUT
    )
)
