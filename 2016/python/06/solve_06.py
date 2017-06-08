"""
EXERCISE PROMPT: http://adventofcode.com/2016/day/6
"""

INPUT = (x.strip('\n') for x in open('input.txt'))

cols  = (sorted(((x, c.count(x))for x in set(c)), key=lambda x: x[1], reverse=True) for c in list(zip(*INPUT)))

msg_A = "".join([x[0][0] for x in cols])

print(msg_A)                                                          # output Part A solution
