"""
EXERCISE PROMPT: http://adventofcode.com/2020/day/10
"""
from collections import Counter, OrderedDict

from itertools import combinations, groupby

INPUT = [int(n.strip('\n'))	for n in open('input', mode='r', encoding='utf-8')]


# universal
nums  = [0] + sorted(INPUT) + [max(INPUT) + 3]
diffs = [b-a for a, b in zip(nums, nums[1:])]


# part A solution:
counts = Counter(diffs)
print(counts[1] * counts[3])

# part B solution:
bottlenecks = sorted({x for diff, n in zip(diffs, nums) for x in {n,n+3} if all((diff == 3, x in nums))})

grouper     = groupby(nums, key=(lambda x: x in bottlenecks))
subsections = list(dict(enumerate((list(j) for i, j in grouper if not i), 1)).values())

subpaths = [[item for sublist in [list(combinations(sp, l)) for l in range(1, len(sp)+1)] for item in sublist] for sp in subsections]
subpaths[0].pop(1) # cannot skip origin so (1,) is removed from [(0,), (1,), (0, 1)] as it is not a valid starting subpath


# for sc in subpaths:
# 	print(sc)

# print(bottlenecks)


"""
Leaving this as a reference point, as I'm now stuck on this approach.

I've organised path combinations by pulling out *consecutive* numbers that have
a difference of 3.

We'll call these "mandatory numbers", because *all* of them are *required*
to be visited by any path given the exercise constraint of not being able
to make n > 3 leaps.

This also means that these "mandatory numbers" are useless when it comes to
generating unique paths. The graph in this excercise is directed and acyclical,


            A                  D
              \              /
               \            /
                \          /
        B ----[ MN ]-->--[ MN ]---- E
                /
               /
              /
            C

so {AD, AE, BD, BE, CD, CE} sufficiently expresses the possible unique paths
that exist, abstracting away the "mandatory numbers/nodes" in between.

We can thus predetermine each possible subpath. I'm now at the frustrating
point where I feel like I "basically have it", but I'm stuck in terms of
a computational approach to make anything of this.

subpaths:
[
	[(0,), (0, 1)]
	[(6,), (7,), (8,), (6, 7), (6, 8), (7, 8), (6, 7, 8)]
	[(16,), (17,), (18,), (16, 17), (16, 18), (17, 18), (16, 17, 18)]
	[(23,), (24,), (25,), (23, 24), (23, 25), (24, 25), (23, 24, 25)]
	[(33,), (34,), (33, 34)]
	[(39,), (40,), (41,), (39, 40), (39, 41), (40, 41), (39, 40, 41)]
	[(46,)]
	[(51,), (52,), (51, 52)]
	[(57,), (58,), (57, 58)]
	[(63,), (64,), (65,), (63, 64), (63, 65), (64, 65), (63, 64, 65)]
	[(73,), (74,), (75,), (73, 74), (73, 75), (74, 75), (73, 74, 75)]
	[(80,), (81,), (82,), (80, 81), (80, 82), (81, 82), (80, 81, 82)]
	[(87,), (88,), (89,), (87, 88), (87, 89), (88, 89), (87, 88, 89)]
	[(94,), (95,), (96,), (94, 95), (94, 96), (95, 96), (94, 95, 96)]
	[(101,), (102,), (101, 102)]
	[(110,)]
	[(115,), (116,), (117,), (115, 116), (115, 117), (116, 117), (115, 116, 117)]
	[(126,), (127,), (128,), (126, 127), (126, 128), (127, 128), (126, 127, 128)]
	[(140,), (141,), (140, 141)]
	[(146,), (147,), (148,), (146, 147), (146, 148), (147, 148), (146, 147, 148)]
]

bottlenecks:
[2, 5, 9, 12, 15, 19, 22, 26, 29, 32, 35, 38, 42, 45, 47, 50, 53, 56, 59, 62, 66, 69, 72, 76, 79, 83, 86, 90, 93, 97, 100, 103, 106, 109, 111, 114, 118, 121, 122, 125, 129, 132, 135, 136, 139, 142, 145, 149, 152]

"""
