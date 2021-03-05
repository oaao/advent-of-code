"""
EXERCISE PROMPT: http://adventofcode.com/2020/day/10
"""
from typing import Dict, List

from collections import defaultdict
import networkx as nx

INPUT = [int(n.strip('\n'))	for n in open('input', mode='r', encoding='utf-8')]


def get_differences(nums):

	diff_counter = defaultdict(int)
	
	nums = [0] + sorted(INPUT) + [max(INPUT) + 3]
	seq  = list(zip(nums, nums[1:]))

	for a, b in seq:
		diff_counter[b - a] += 1

	return diff_counter


def build_graph_dict(nums):

	graph_dict = {n: [] for n in nums}

	for k in graph_dict:
		for n in nums:
			if 1 <= n-k <= 3:
				graph_dict[k].append(n)

	return graph_dict


def get_valid_combo_count(graph_dict):

	g     = nx.DiGraph(graph_dict)
	paths = nx.all_simple_paths(g, min(graph_dict), max(graph_dict))

	count = 0

	for path in paths:
		count += 1

	return count


# part A solution:
dc = get_differences(INPUT)
print(dc[1] * dc[3])

# part B solution: this won't even run
print(get_valid_combo_count(build_graph_dict(INPUT)))