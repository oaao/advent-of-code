"""
EXERCISE PROMPT: http://adventofcode.com/2020/day/4
"""

from typing import List, Dict

import string
from itertools import groupby


INPUT = [
			field
			for line in open('input', mode='r', encoding='utf-8')
			for field in line.strip('\n').split(' ')
		]


def generate_passports(data: List[str]) -> List[Dict[str, str]]:

	grouped = (
		list(val)
		for _bool, val in groupby(INPUT, lambda delim: delim == '') if not _bool
	)

	parsed  = (
		dict(term.split(':') for term in passport)
		for passport in grouped
	) 

	return parsed


def validate_passport(passport: List[Dict[str, str]]) -> Dict[str, bool]:

	byr, iyr, eyr, hgt, hcl, ecl, pid = [
		passport.get(x)
		for x in ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')
	]

	criteria = {
		'byr': 1920 <= int(byr) <= 2002,
		'iyr': 2010 <= int(iyr) <= 2020,
		'eyr': 2020 <= int(eyr) <= 2030,
		'hgt': any((
			150 <= int(hgt.strip('cm')) <= 193 if hgt.endswith('cm') else False,
			59  <= int(hgt.strip('in')) <= 76  if hgt.endswith('in') else False,
		)),
		'hcl': all((
			hcl[0] == '#',
			all(c in string.hexdigits for c in hcl[1:])
		)),
		'ecl': ecl in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'},
		'pid': all((
			len(pid) == 9,
			all(c.isdigit() for c in pid)
		))
	}

	return criteria


# part A solution
complete_passports: List[Dict[str, str]] = list(
	passport for passport in generate_passports(INPUT)
	if all(k in passport for k in {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'})
)

print(len(complete_passports))

# part B solution
valid_passports: List[Dict[str, str]] = list(
	passport for passport in complete_passports
	if all(validate_passport(passport).values())
)
print(len(valid_passports))