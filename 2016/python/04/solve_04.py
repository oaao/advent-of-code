"""
EXERCISE PROMPT: http://adventofcode.com/2016/day/4
"""

INPUT = (x.strip('\n').strip(']').split('[') for x in open('input.txt'))        # pls no regex


def validate_code(code):

    c, i, s = code[0][:-4], int(code[0][-3:]), code[1]                # codename, ID, checksum

    if all(x in c for x in s):                                        # bail unless entire checksum present

        q = sorted(((x, c.count(x)) for x in set(c.replace('-', ''))), key=lambda x: x[1], reverse=True)
        m = min(list(zip(*q))[1][:5])

        d = {}                                                        # rip nice expressions w/o operator or collections
        for x, n in q:
            if n > m:
                d.setdefault(n, []).append(x)                         # group by freq to solve ties at each freq later
            elif n == m and x in s:                                   # min req freq chars also need checksum membership
                d.setdefault(n, []).append(x)

        f = "".join(["".join(sorted(x)) for x in d.values()])         # since e.g. 'a' < 'b' returns True, sort at each
                                                                      # freq group to alphabetise, then flatten it all
        if f == s:
            return c, i, s

valid_rooms = list(filter(None, (validate_code(x) for x in INPUT)))   # no return for an invalid room, so filter those

print(sum([i for c, i, s in valid_rooms]))                            # output part A answer
