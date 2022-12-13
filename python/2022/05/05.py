"""
EXERCISE PROMPT: http://adventofcode.com/2022/day/5
"""
import copy

INPUT = tuple(open("input", "r", encoding="utf-8").read().rstrip().split("\n"))
split_at = INPUT.index("")

# process stack into useful input
stacks = dict(
    (int(stack[0]), list(x for x in stack[1:] if x not in (" ", None)))
    for stack in zip(*reversed(INPUT[:split_at]))
    if stack[0] != " "
)

instructions = tuple(
    # n crates, from, to
    tuple(
        map(
            int,
            instr.replace("move ", "")
            .replace(" from", "")
            .replace(" to", "")
            .split(" "),
        )
    )
    for instr in INPUT[split_at + 1 :]
)


def get_message(one_by_one: bool) -> str:
    stacks_ = copy.deepcopy(stacks)
    for n, from_, to_ in instructions:
        substack = (  # subscribe
            reversed(stacks_[from_][-n:]) if one_by_one else stacks_[from_][-n:]
        )
        stacks_[to_].extend(substack)
        del stacks_[from_][-n:]
    return "".join(stack[-1] for stack in stacks_.values())


# part A solution
print(get_message(one_by_one=True))

# part B solution
print(get_message(one_by_one=False))
