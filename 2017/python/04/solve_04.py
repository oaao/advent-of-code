"""
EXERCISE PROMPT: http://adventofcode.com/2017/day/4
"""

# independent solutions with a lot of duplicate code; dedupe and clean up
print(len([r for r in open('input.txt') if len(r.split()) == len(set(r.split()))]))                                                             # part A answer
print(len([r for r in open('input.txt') if len([''.join(sorted(x)) for x in r.split()]) == len(set(''.join(sorted(x)) for x in r.split()))]))   # part B solution
