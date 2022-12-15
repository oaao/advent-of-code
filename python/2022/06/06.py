"""
EXERCISE PROMPT: http://adventofcode.com/2022/day/6
"""

INPUT = open("input", "r", encoding="utf-8").read().strip()

# part A solution
print(
    next(
        n
        for n, seq in enumerate(
            zip(INPUT, INPUT[1:], INPUT[2:], INPUT[3:]),
            start=4,
        )
        if len(seq) == len(set(seq))
    )
)
