"""
EXERCISE PROMPT: http://adventofcode.com/2018/day/1
"""

INPUT = open('input.txt', mode='r', encoding='UTF-8')

solution_A = sum(int(n) for n in INPUT)

print(solution_A)
