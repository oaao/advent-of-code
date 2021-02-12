"""
EXERCISE PROMPT: http://adventofcode.com/2020/day/7
"""

from typing import Dict, List


INPUT = [
	bag.strip('.\n').replace(' bags', '').replace(' bag', '').split(' contain ')
	for bag in open('input', mode='r', encoding='utf-8')
]


def build_ruleset(data: List[str]):

	return {
		bag: {
			b[2:]: int(b[0]) for b in contents.split(', ') if b != 'no other'
		} 
		for bag, contents in data
	}


def get_outermost_bags(ruleset: Dict[str, Dict[str, int]], target_bag: str) -> set:

	outermost_bags = set()

	def recursive_parentage(ruleset, target_bag):
		for bag, contents in ruleset.items():
			if target_bag in contents:
				outermost_bags.add(bag)
				recursive_parentage(ruleset, bag)

	recursive_parentage(ruleset, target_bag)

	return outermost_bags


def get_bag_nesting(ruleset: Dict[str, Dict[str, int]], target_bag: str) -> Dict[str, int]:

	bag_tally = dict()

	def recursive_nesting(ruleset, target_bag):

		for bag, count in ruleset[target_bag].items():

			if bag in bag_tally:
				bag_tally[bag] += count
			else: 
				bag_tally[bag] =  count

			for x in range(count):
				recursive_nesting(ruleset, bag)

	recursive_nesting(ruleset, target_bag)

	return bag_tally


ruleset = build_ruleset(INPUT)

# part A solution
print(len(get_outermost_bags(ruleset, 'shiny gold')))
# part B solution
print(sum(get_bag_nesting(ruleset, 'shiny gold').values()))
