"""
EXERCISE PROMPT: http://adventofcode.com/2018/day/2
"""

from collections import Counter

INPUT = [_.strip('\n') for _ in open('input.txt', mode='r', encoding='UTF-8')]

# part A
def checksum_counts(s):

    c = Counter(s)

    return {v for k, v in c.items() if (v==2 or v==3)}

# use sum(iterable, start_val) syntax: sum(counter_list, Counter())
# otherwise, 0 is the default start value and int+Counter --> TypeError
factors = sum([Counter(checksum_counts(c)) for c in INPUT], Counter())


# part B
def get_diff_by_one(diffs):

    for a in diffs:
        for b in diffs:

            diff = 0

            for i in range(len(a)):
                if a[i] != b[i]:
                    diff += 1

            if diff == 1:
                common = [a[i] for i in range(len(a)) if a[i] == b[i]]

                return ''.join(common)


print(f'A: {factors[2] * factors[3]}')
print(f'B: {get_diff_by_one(INPUT)}')
