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
    root_values = []

    for n in range(child_nodes):
        total, root_value, data = parse_tree(data)
        meta_total            += total
        root_values.append(root_value)

    meta_total += sum(data[:meta_count])

    if child_nodes ==0:
        return(meta_total, sum(data[:meta_count]), data[meta_count:])
    else:
        return(
            meta_total,
            sum(root_values[n-1] for n in data[:meta_count] if n > 0 and n <= len(root_values)),
            data[meta_count:]
        )

total, root_value, remaining_data = parse_tree(INPUT)

# part A solution:
print(f'A: {total}')
print(f'B: {root_value}')