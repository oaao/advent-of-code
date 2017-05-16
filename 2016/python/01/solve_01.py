"""
EXERCISE PROMPT: http://adventofcode.com/2016/day/1
"""

INPUT = ["R3", "L2", "L2", "R4", "L1", "R2", "R3", "R4", "L2", "R4", "L2", "L5", "L1", "R5", "R2", "R2", "L1", "R4", "R1", "L5", "L3", "R4", "R3", "R1", "L1", "L5", "L4", "L2", "R5", "L3", "L4", "R3", "R1", "L3", "R1", "L3", "R3", "L4", "R2", "R5", "L190", "R2", "L3", "R47", "R4", "L3", "R78", "L1", "R3", "R190", "R4", "L3", "R4", "R2", "R5", "R3", "R4", "R3", "L1", "L4", "R3", "L4", "R1", "L4", "L5", "R3", "L3", "L4", "R1", "R2", "L4", "L3", "R3", "R3", "L2", "L5", "R1", "L4", "L1", "R5", "L5", "R1", "R5", "L4", "R2", "L2", "R1", "L5", "L4", "R4", "R4", "R3", "R2", "R3", "L1", "R4", "R5", "L2", "L5", "L4", "L1", "R4", "L4", "R4", "L4", "R1", "R5", "L1", "R1", "L5", "R5", "R1", "R1", "L3", "L1", "R4", "L1", "L4", "L4", "L3", "R1", "R4", "R1", "R1", "R2", "L5", "L2", "R4", "L1", "R3", "L5", "L2", "R5", "L4", "R5", "L5", "R3", "R4", "L3", "L3", "L2", "R2", "L5", "L5", "R3", "R4", "R3", "R4", "R3", "R1"]


def direction_ctrl(dist):
    return [(0, dist), (dist, 0), (0, -dist), (-dist, 0)]    # [north, east, south, west] movement cases


def get_vectors(instructions):

    direction = 0  # begin facing north
    vectors   = []

    vect_pairs = [(x[0], int(x[1:])) for x in instructions]  # create list of (direction, distance) tuples

    for v in vect_pairs:
        vect_dir  = v[0]
        vect_dist = v[1]
        if vect_dir == 'R':                                  # track direction changes with CW/CCW turns
            direction = (direction + 1) % 4
        if vect_dir == 'L':
            direction = (direction - 1) % 4
        vector = direction_ctrl(vect_dist)[direction]        # store new vector from direction controller
        vectors.append(vector)

    return vectors


def shortest_path(vectors):                                  # establish Part 1 solution

    coord = (0,0)

    for v in vectors:
        coord = tuple([a + b for a, b in zip(v, coord)])

    return abs(coord[0]) + abs(coord[1])

# print(shortest_path(get_vectors(INPUT)))                     # output Part 1 solution
