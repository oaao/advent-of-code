"""
EXERCISE PROMPT: http://adventofcode.com/2023/day/1
"""

INPUT = [s.strip("\n") for s in open("input", mode="r", encoding="utf-8")]


# solutions
A = sum(
	map(
		int, (line[0] + line[-1] 
		for line in (
			list(filter(str.isdigit, line)) for line in INPUT)
		)
	)
)
