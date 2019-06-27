"""
EXERCISE PROMPT: http://adventofcode.com/2018/day/1
"""
from itertools import accumulate, cycle

INPUT = open('input.txt', mode='r', encoding='UTF-8').readlines()

# part A
freq_deltas = [int(n) for n in INPUT]

# part B
seen = {0}     # rather than initialise an empty set,
               # we account for a +n -n input start

first_repeated = next(
    f for f in accumulate(cycle(freq_deltas)) \
    if f in seen                              \
    or seen.add(f)
)

print(f'A: {sum(freq_deltas)}')
print(f'B: {first_repeated}')
