"""
EXERCISE PROMPT: http://adventofcode.com/2016/day/2
"""

INPUT = list(x.strip('\n') for x in open('input.txt'))               # get rid of newline; it is not a valid "move"

instr = {
    'U':  (0, 1),
    'D':  (0, -1),
    'R':  (1, 0),
    'L':  (-1, 0)
}

kp_A = [(x, y) for y in range(1, -2, -1) for x in range(-1, 2)]      # generate regular grid of Part A's keypad


def bound(x, mi, ma):                                                # disallow movement beyond keypad edges
    return max(min(x, ma), mi)


def kp_nav(moves, start, kp):

    coord  = start
    unique = set(sum(kp, ()))                                        # fastest way to flatten and de-duplicate coords
    mi, ma = min(unique), max(unique)

    for m in moves:
        unbound = (ta + tb for ta, tb in zip(coord, instr[m]))
        coord   = tuple(bound(x, mi, ma) for x in unbound)

    return coord

code_A = [kp_A.index(kp_nav(m, (0, 0), kp_A)) + 1 for m in INPUT]    # look up keypad number for each instruction line

print(''.join(map(str, code_A)))                                     # output Part A solution
