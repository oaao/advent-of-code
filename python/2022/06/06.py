"""
EXERCISE PROMPT: http://adventofcode.com/2022/day/6
"""

INPUT = open("input", "r", encoding="utf-8").read().strip()


def count_buffer(marker_len: int) -> int:
    return next(
        n
        for n, seq in enumerate(
            zip(*(INPUT[n:] for n in range(marker_len))),
            start=marker_len,
        )
        if len(seq) == len(set(seq))
    )


# part A solution
print(count_buffer(4))


# part B solution
print(count_buffer(14))
