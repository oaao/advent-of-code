"""
EXERCISE PROMPT: http://adventofcode.com/2020/day/1
"""

INPUT = [int(n.strip('\n')) for n in open('input', mode='r', encoding='utf-8')]


# part A
"""
for a in INPUT:
	for b in INPUT:
		if a + b == 2020:
			a * b
"""
entry_pair    = {(a * b) for a in INPUT for b in INPUT if a + b == 2020}

# part B 
entry_triplet = {(a * b * c) for a in INPUT for b in INPUT for c in INPUT if a + b + c == 2020}

print(entry_pair)    # part A solution
print(entry_triplet) # part B solution
