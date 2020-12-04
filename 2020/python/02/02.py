"""
EXERCISE PROMPT: http://adventofcode.com/2020/day/1
"""
import re

INPUT = [
    re.split(' |-|:', n.strip('\n'))
	for n in open('input', mode='r', encoding='utf-8')
]

valid_passwords_A = set()
valid_passwords_B = set()

# part A
for low, high, char, _, password in INPUT:
	if int(low) <= password.count(char) <= int(high):
		valid_passwords_A.add(password)

# part B
for pos1, pos2, char, _, password in INPUT:
	match = (
		password[int(pos1)-1] == char,        # no 0-index in input
		password[int(pos2)-1] == char         # "
	)
	if any(match) and not all(match):         # one can match, but not both
		valid_passwords_B.add(password)

print(len(valid_passwords_A)) # part A solution
print(len(valid_passwords_B)) # part A solution
