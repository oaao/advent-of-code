"""
EXERCISE PROMPT: http://adventofcode.com/2022/day/4
"""
import itertools

INPUT = tuple(
    tuple(
        tuple(map(int, section.split("-")))
        for section in line.split(",")
    )
    for line in open("sample", "r", encoding="utf-8").read().strip().split("\n")
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
