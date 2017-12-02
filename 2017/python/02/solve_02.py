"""
EXERCISE PROMPT: http://adventofcode.com/2017/day/2
"""

INPUT = ([int(x) for x in row.strip('\n').split('\t')] for row in open('input.txt', mode='r', encoding='UTF-8'))

print(sum((max(x) - min(x)) for x in INPUT))    # part A solution
