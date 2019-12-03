"""
EXERCISE PROMPT: http://adventofcode.com/2019/day/2
"""

from itertools import permutations, zip_longest
from functools import partialmethod


INPUT = [int(n) for n in open('input.txt', mode='r', encoding='utf-8').read().split(',')]


def run_intcoder(intcodes, noun, verb, instr_length=4):

    state    = intcodes.copy()
    state[1] = noun
    state[2] = verb

    _reshape     = [iter(intcodes)] * instr_length
    instructions = zip_longest(*_reshape, fillvalue=None)

    for op, a, b, loc in instructions:

        if   op == 1:
            state[loc] = state[a] + state[b]
        elif op == 2:
            state[loc] = state[a] * state[b]
        elif op == 99:
            return state
        elif op not in ([1, 2, 99]):
            raise ValueError(f'invalid opcode {op} in instruction {(op, a, b, loc)}')

    return state


def bruteforce_pair(lowest, highest, output_match):

    pairs = permutations(range(lowest, highest+1), 2)

    for p in pairs:

        result = run_intcoder(INPUT, *p)
        # print(f'Ran: {p}, got: {result[0]}')

        if result[0] == output_match:
            return p


# part A solution
print(f'A: {run_intcoder(INPUT, 12, 2)[0]}')

# part B solution
noun, verb = bruteforce_pair(0, 99, 19690720)
print(f'B: {100 * noun + verb}')