"""
EXERCISE PROMPT: http://adventofcode.com/2018/day/7
"""

# >importing re lmao

from sys import maxsize

INPUT = [
    (x[1], x[7])
    for x in
    [s.strip('\n').split(' ') for s in open('input.txt')]
]


print(INPUT[0])


# cheaty flattening method: see 2018/02 {factors}
steps = set(sum(INPUT, ()))


# part A solution
def get_next_step(steps, orderings):
    return [
        step for step in steps
        if all(subsequent != step for (_, subsequent) in orderings)
    ]

def get_step_sequence(step_set, order):

    orderings = order.copy()
    steps     = step_set.copy()

    order = ''

    while steps:

        possible = list(get_next_step(steps, orderings))
        possible.sort()

        s = possible[0]
        order += s

        steps.remove(s)
        orderings = [(a, b) for (a, b) in orderings if a != s]

    return order


# part B solution
def get_time(s):
    return ord(s) - ord('A') + 60

def get_total_time(step_set, order, worker_count=5):

    orderings = order.copy()
    steps     = step_set.copy()

    t = 0

    workers = [0    for _ in range(worker_count)]
    work    = [None for _ in range(worker_count)]

    while steps or any(w > 0 for w in workers):

        possible = list(get_next_step(steps, orderings))
        possible.sort(reverse=True)
        print(t, possible, workers, work, len(steps), len(orderings))

        for worker in range(worker_count):
            print(workers[worker], possible)

            workers[worker] = max(workers[worker] - 1, 0)

            if workers[worker] == 0:
                if work[worker] is not None:
                    orderings = [(a, b) for (a, b) in orderings if a != work[worker]]

            if possible:
                s = possible.pop()
                workers[worker] = get_time(s)
                work[worker]    = s
                steps.remove(s)

        t += 1

    return t



print(f'A: {get_step_sequence(steps, INPUT)}')
print(get_total_time(steps, INPUT))