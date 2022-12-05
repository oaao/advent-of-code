"""
EXERCISE PROMPT: http://adventofcode.com/2016/day/1
"""

INPUT = ["R3", "L2", "L2", "R4", "L1", "R2", "R3", "R4", "L2", "R4", "L2", "L5", "L1", "R5", "R2", "R2", "L1", "R4", "R1", "L5", "L3", "R4", "R3", "R1", "L1", "L5", "L4", "L2", "R5", "L3", "L4", "R3", "R1", "L3", "R1", "L3", "R3", "L4", "R2", "R5", "L190", "R2", "L3", "R47", "R4", "L3", "R78", "L1", "R3", "R190", "R4", "L3", "R4", "R2", "R5", "R3", "R4", "R3", "L1", "L4", "R3", "L4", "R1", "L4", "L5", "R3", "L3", "L4", "R1", "R2", "L4", "L3", "R3", "R3", "L2", "L5", "R1", "L4", "L1", "R5", "L5", "R1", "R5", "L4", "R2", "L2", "R1", "L5", "L4", "R4", "R4", "R3", "R2", "R3", "L1", "R4", "R5", "L2", "L5", "L4", "L1", "R4", "L4", "R4", "L4", "R1", "R5", "L1", "R1", "L5", "R5", "R1", "R1", "L3", "L1", "R4", "L1", "L4", "L4", "L3", "R1", "R4", "R1", "R1", "R2", "L5", "L2", "R4", "L1", "R3", "L5", "L2", "R5", "L4", "R5", "L5", "R3", "R4", "L3", "L3", "L2", "R2", "L5", "L5", "R3", "R4", "R3", "R4", "R3", "R1"]


def direction_ctrl(dist):
    return (0, dist), (dist, 0), (0, -dist), (-dist, 0)                    # [north, east, south, west] movement cases


def get_vectors(instructions):

    direction = 0  # begin facing north
    vectors   = []

    vect_pairs = [(x[0], int(x[1:])) for x in instructions]                # create list of (direction, distance) tuples

    for v_dir, v_dist in vect_pairs:
        if v_dir == 'R':                                                   # track direction changes with CW/CCW turns
            direction = (direction + 1) % 4

        if v_dir == 'L':
            direction = (direction - 1) % 4
        vector = direction_ctrl(v_dist)[direction]                         # store new vector from direction controller
        vectors.append(vector)

    return vectors


def get_shortest(vectors):                                                 # establish Part 1 solution

    coord = (0,0)
    for vector in vectors:
        coord = tuple((a + b for a, b in zip(vector, coord)))

    return abs(coord[0]) + abs(coord[1])


def first_repeated(v_steps):

    # below are war crimes. find a better way to do this.
    v_incr = []
    coords = [(0, 0), ]

    for a, b in v_steps:
        diff = max(abs(a), abs(b))
        incr = -1 if a < 0 or b < 0 else 1
        v_incr.append([(0, incr)] * diff if a == 0 else [(incr, 0)] * diff)

    v_indiv = (c for x in v_incr for c in x)

    for v in v_indiv:
        if len(coords) == len(set(coords)):
            coords.append(tuple([a + b for a, b in zip(v, coords[-1])]))

    return abs(coords[-1][0]) + abs(coords[-1][1])

vects = get_vectors(INPUT)

print(get_shortest(vects))                                                  # output Part 1 solution
print(first_repeated(vects))                                                # output Part 2 solution
