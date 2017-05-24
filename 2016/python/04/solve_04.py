"""
EXERCISE PROMPT: http://adventofcode.com/2016/day/4
"""

INPUT = (x.strip('\n').strip(']').replace('-', '').split('[') for x in open('input.txt'))  # pls no regex

# a) separate code and sector ID, and filter out codes where all checksum chars are not present
has_all_chksm = (
                    (c[:-3], c[-3:], s)
                    for c, s in INPUT
                    if all(x in c for x in s)
                )

# b) filter out instances where the five checksum characters are not the five most used
freqs = (reversed(list(
                        sorted(
                            ((x, i[0].count(x)) for x in set(i[0])),
                            key=lambda x: x[1]
                            )
                        )
                  ) for i in list(has_all_chksm))

# chksm_most = ((c, i, s) for c, i, s in has_all_chksm if all(list(zip(*x))[0][:5] in c for x in freqs))

# for i in freqs:
#    all(list(zip(*i))[0][:5] for i in freqs)

# c) use 'a' < 'b' comparison to determine alphabetical order for ties ('a' < 'b', for example, returns True)
