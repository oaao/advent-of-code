"""
EXERCISE PROMPT: http://adventofcode.com/2018/day/8
"""

from string import ascii_uppercase as alphabet
import pprint


INPUT = [int(i) for i in open('input.txt').read().strip('\n').split(' ')]


def parse_tree(data):

    child_nodes, meta_count = data[:2]
    data                 = data[2:]

    meta_total = 0

    for n in range(child_nodes):
        total, data = parse_tree(data)
        meta_total     += total

    meta_total += sum(data[:meta_count])

    return(meta_total, data[meta_count:])

total, remaining_data = parse_tree(INPUT)

# part A solution:
print(f'A: {total}')
