"""
EXERCISE PROMPT: http://adventofcode.com/2022/day/3
"""
from string import ascii_letters

INPUT = tuple(open("input", "r", encoding="utf-8").read().strip().split("\n"))

priority_map = {chr: n for n, chr in enumerate(ascii_letters, start=1)}

as_priorities = tuple(
    tuple(
        map(lambda chr: priority_map[chr], s)
    ) for s in INPUT
)

# part A solution: we can use sets, since we want type occurrence not instance occurrence  
print(
    sum(
        next(iter(
            set(ruck[:len(ruck) // 2]).intersection(set(ruck[(len(ruck) // 2):]))
        )) for ruck in as_priorities
    )
)
