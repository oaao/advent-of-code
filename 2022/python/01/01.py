"""
EXERCISE PROMPT: http://adventofcode.com/2022/day/1
"""
import itertools

INPUT = [s.strip("\n") for s in open("input", mode="r", encoding="utf-8")]

groups = tuple(
    tuple(map(int, s))
    for k, s in itertools.groupby(INPUT, lambda delim: delim == "")
    if not k
)

# part A
print(max(map(sum, groups)))

# part B
print(sum(sorted(map(sum, groups))[-3:]))
