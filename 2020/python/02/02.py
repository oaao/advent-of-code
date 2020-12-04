"""
EXERCISE PROMPT: http://adventofcode.com/2020/day/1
"""
import re

INPUT = [
    re.split(' |-|:', n.strip('\n'))
	for n in open('input', mode='r', encoding='utf-8')
]

valid_passwords = set()

for low, high, char, _, password in INPUT:
	if int(low) <= password.count(char) <= int(high):
		valid_passwords.add(password)

# part A solution
print(len(valid_passwords))
