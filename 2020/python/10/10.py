"""
EXERCISE PROMPT: http://adventofcode.com/2020/day/10
"""
from typing import Dict, List

from collections import defaultdict

INPUT = [int(n.strip('\n'))	for n in open('input', mode='r', encoding='utf-8')]


def get_differences(nums):

	diff_counter = defaultdict(int)
	seq = list(zip(nums, nums[1:]))

	for a, b in seq:
		diff_counter[b - a] += 1

	return diff_counter


def build_adapter_graph(nums):

	graph = {n: [] for n in nums}

	for k in graph:
		for n in nums:
			if 1 <= n-k <= 3:
				graph[k].append(n)

	return graph


def get_adapter_arrangements(nums):
	
	def get_valid_paths(graph, start_node, path=[]):

		path  = path + [start_node]
		paths = [path]

		for node in graph[start_node]:
			subpaths = get_valid_paths(graph, node, path)
			for s in subpaths:
				paths.append(s)

		return paths


	graph        = build_adapter_graph(sorted(nums))
	arrangements = get_valid_paths(graph, min(nums))

	return arrangements

# universal
nums = [0] + sorted(INPUT) + [max(INPUT) + 3]

# part A solution:
dc = get_differences(nums)
print(dc[1] * dc[3])

# part B solution: this won't even run
print(len(get_adapter_arrangements))
