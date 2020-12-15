"""
EXERCISE PROMPT: http://adventofcode.com/2020/day/4
"""

from typing import List, Dict

from itertools import groupby

INPUT = [
			field
			for line in open('input', mode='r', encoding='utf-8')
			for field in line.strip('\n').split(' ')
		]


def generate_passports(data: List[str]) -> List[List[str]]:

	grouped = (
		list(val)
		for _bool, val in groupby(INPUT, lambda delim: delim == '') if not _bool
	)

	parsed  = (
		dict(term.split(':') for term in passport)
		for passport in grouped
	) 

	return parsed


# part A solution
print(
	len([
		passport for passport in generate_passports(INPUT)
		if all (k in passport for k in {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'})
	])
)
