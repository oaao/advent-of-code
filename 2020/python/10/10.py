"""
EXERCISE PROMPT: http://adventofcode.com/2020/day/10
"""

from collections import Counter

INPUT = [int(n.strip('\n'))	for n in open('input', mode='r', encoding='utf-8')]


# universal
nums = [0] + sorted(INPUT) + [max(INPUT) + 3]

# part A solution:
diffs = [b-a for a, b in zip(nums, nums[1:])]
counts = Counter(diffs)
print(counts[1] * counts[3])
