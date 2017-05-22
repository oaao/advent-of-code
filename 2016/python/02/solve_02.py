"""
EXERCISE PROMPT: http://adventofcode.com/2016/day/2
"""

INPUT = list(x.strip('\n') for x in open('input.txt'))                 # get rid of newline; it is not a valid "move"

instr = {
    'U':  (0, 1),
    'D':  (0, -1),
    'R':  (1, 0),
    'L':  (-1, 0)
}

# change everything to use sets/enumerate() - list lookups feel kinda dirty


def kp_gen(size, pad):                                                 # generic construction of keypads

    d      = int((abs(size) - 1) / 2) if size % 2 == 1 else 0

    kp_all = list((x, y) for y in range(d, -(d + 1), -1) for x in range(-d, d + 1))
    kp     = list(filter(lambda x: abs(x[0]) * abs(x[1]) < pad, kp_all)) if pad != 0 else kp_all

    return kp


def kp_nav(moves, start, kp):

    coord  = start

    for m in moves:
        next  = tuple(ta + tb for ta, tb in zip(coord, instr[m]))
        coord = next if next in kp else coord                          # membership check - much faster if set vs. list

    return coord


kp_A   = kp_gen(3, 0)
code_A = list(kp_A.index(kp_nav(c, (0, 0), kp_A)) + 1 for c in INPUT)  # look up keypad number for each instruction line

kp_B   = kp_gen(5, 2)
code_B = list(kp_B.index(kp_nav(c, (-2, 0), kp_B)) + 1 for c in INPUT)

print(''.join(map(str, code_A)))                                       # output Part A solution
print(''.join(map(lambda x: hex(x)[2:], code_B)))                      # output Part B solution
