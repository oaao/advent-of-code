"""
EXERCISE PROMPT: http://adventofcode.com/2016/day/2
"""

INPUT     = list(list(int(s) for s in x.split()) for x in open('input.txt'))

possible  = list(filter(lambda x: sum(x) > max(x) * 2, INPUT))                  # no need to sort or overcomplicate

print(len(possible))                                                            # output Part A answer
