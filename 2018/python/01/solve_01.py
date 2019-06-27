"""
EXERCISE PROMPT: http://adventofcode.com/2018/day/1
"""
from itertools import accumulate, cycle

INPUT = open('input.txt', mode='r', encoding='UTF-8').readlines()

# part A
freq_deltas = [int(n) for n in INPUT]

print(f'A: {sum(freq_deltas)}')
