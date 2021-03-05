"""
EXERCISE PROMPT: http://adventofcode.com/2020/day/10
"""

from collections import Counter
from functools import lru_cache

INPUT = [int(n.strip('\n'))	for n in open('input', mode='r', encoding='utf-8')]


def build_graph(nums):

	graph = {n: [] for n in nums}

	for k in graph:
		for n in nums:
			if 1 <= n-k <= 3:
				graph[k].append(n)

	return graph


def get_paths(graph, start_node, end_node):

	cache = dict()

	def dfs(node):

		if node not in cache:

			if node == end_node:
				cache[node] = [[end_node]]
			
			else:
				# if graph is potentially cyclical, mark current path like so
				# cache[node] = None
				cache[node] = [
					[node] + path
					for connected_node in graph[node] for path in dfs(connected_node) if path
				]

		return cache[node]

	return dfs(start_node)


# universal
nums = [0] + sorted(INPUT) + [max(INPUT) + 3]

# part A solution:
diffs = [b-a for a, b in zip(nums, nums[1:])]
counts = Counter(diffs)
print(counts[1] * counts[3])

# part B solution:
graph = build_graph(nums)
print(len(get_paths(graph, 0, max(nums))))
