"""
EXERCISE PROMPT: http://adventofcode.com/2019/day/2
"""

from itertools import zip_longest


INPUT = [int(n) for n in open('input.txt', mode='r', encoding='utf-8').read().split(',')]


def run_intcoder(intcodes, _a, _b, instr_length=4):

    state    = intcodes
    state[1] = _a
    state[2] = _b

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


# part A solution
print(f'A: {run_intcoder(INPUT, 12, 2)[0]}')
