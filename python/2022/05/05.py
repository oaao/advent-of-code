"""
EXERCISE PROMPT: http://adventofcode.com/2022/day/5
"""
from itertools import zip_longest

INPUT    = tuple(open("sample", "r", encoding="utf-8").read().strip().split('\n'))
split_at = INPUT.index("")

# process stack into useful input
stacks = dict(
    (int(stack[0]), list(x for x in stack[1:] if x not in (" ", None)))
    for stack in zip_longest(*reversed(INPUT[:split_at]))
    if stack[0] != " "
)

instructions = tuple(
    tuple(
        map(
            int,
            instr.replace("move ", "").replace(" from", "").replace(" to", "").split(" ")
        )
    )
    for instr in INPUT[split_at + 1:]
)

print(instructions)