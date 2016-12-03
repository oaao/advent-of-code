"""
--- Day 1: No Time for a Taxicab ---
http://adventofcode.com/2016/day/1

... The Document indicates that you should start at the given coordinates (where you just landed) and face North.
Then, follow the provided sequence: either turn left (L) or right (R) 90 degrees, then walk forward the given number
of blocks, ending at a new intersection...

Given that you can only walk on the street grid of the city, how far is the shortest path to the destination?

[inputs provided as below]

"""

WALK_DIRECTIONS = ["R3", "L2", "L2", "R4", "L1", "R2", "R3", "R4", "L2", "R4", "L2", "L5", "L1", "R5", "R2", "R2", "L1",
                   "R4", "R1", "L5", "L3", "R4", "R3", "R1", "L1", "L5", "L4", "L2", "R5", "L3", "L4", "R3", "R1", "L3",
                   "R1", "L3", "R3", "L4", "R2", "R5", "L190", "R2", "L3", "R47", "R4", "L3", "R78", "L1", "R3", "R190",
                   "R4", "L3", "R4", "R2", "R5", "R3", "R4", "R3", "L1", "L4", "R3", "L4", "R1", "L4", "L5", "R3", "L3",
                   "L4", "R1", "R2", "L4", "L3", "R3", "R3", "L2", "L5", "R1", "L4", "L1", "R5", "L5", "R1", "R5", "L4",
                   "R2", "L2", "R1", "L5", "L4", "R4", "R4", "R3", "R2", "R3", "L1", "R4", "R5", "L2", "L5", "L4", "L1",
                   "R4", "L4", "R4", "L4", "R1", "R5", "L1", "R1", "L5", "R5", "R1", "R1", "L3", "L1", "R4", "L1", "L4",
                   "L4", "L3", "R1", "R4", "R1", "R1", "R2", "L5", "L2", "R4", "L1", "R3", "L5", "L2", "R5", "L4", "R5",
                   "L5", "R3", "R4", "L3", "L3", "L2", "R2", "L5", "L5", "R3", "R4", "R3", "R4", "R3", "R1"]


def dir_ctrl(dist):
    return [(0, dist), (dist, 0), (0, -dist), (-dist, 0)]              # [north, east, south, west] movement cases


def get_shortest_path(vect_list):

    direction = 0                                                      # begin facing north
    coord = (0,0)

    vect_pairs = [(x[0], int(x[1:])) for x in vect_list]               # create list of (direction, distance) tuples

    for vect in vect_pairs:
        vect_dir  = vect[0]
        vect_dist = vect[1]
        if vect_dir == 'R':                                            # track direction changes with CW/CCW turns
            direction = (direction + 1) % 4
        elif vect_dir == 'L':
            direction = (direction - 1) % 4
        else:
            break                                                      # only allowed to turn L or R
        coord_next = dir_ctrl(vect_dist)[direction]                    # store new coord from direction controller
        coord = tuple([a+b for (a,b) in zip(coord, coord_next)])

    return abs(coord[0]) + abs(coord[1])