"""
EXERCISE PROMPT: http://adventofcode.com/2018/day/9
"""

INPUT = [
    tuple(map(int, (x, y, vx, vy)))
    for label_pos, x, y, label_v, vx, vy, tail in
    (s.strip('\n').replace('<', ',').replace('>', ',').split(',') for s in open('input.txt').readlines())
]

# since the problem alludes to all points converging to legibility, and then diverging,
# start near the minimal bounding box:
def predict_smallest_bounds_time(data, duration=20000):

    bounds = dict()

    for i in range(duration):
        min_x = min(x + i * vx for (x, y, vx, vy) in data)
        max_x = max(x + i * vx for (x, y, vx, vy) in data)

        min_y = min(y + i * vx for (x, y, vx, vy) in data)
        max_y = max(y + i * vx for (x, y, vx, vy) in data)

        bounds[((max_x - min_x) * (max_y - min_y))] = i

    smallest_area = min(bounds)

    return smallest_area, bounds[smallest_area]


def display()

bounds, start_time = predict_smallest_bounds_time(INPUT)

display = [[' '] * 200 for n in range(400)]

