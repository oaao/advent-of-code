"""
EXERCISE PROMPT: http://adventofcode.com/2016/day/4
"""

INPUT = (x.strip('\n').strip(']').split('[') for x in open('input.txt'))                                  # pls no regex


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

shifted = [
            (
                ["".join([chr((((ord(x) - 97) + i) % 26) + 97) for x in w])for w in c.split('-')],        # ord(a) is 97
                i
            ) for c, i, s in valid_rooms
          ]

b, = (i for c, i in shifted if 'object' in c)                         # also verifies that there is only one result!

print(sum([i for c, i, s in valid_rooms]))                            # output part A answer
print(b)                                                              # output part B answer

'''
N.B. The result string for Part B is "northpole object storage", while the exercise asks us to look for "the room where
     North Pole objects are stored". We cannot arrive at the result with a membership lookup of "north" or "pole", 
     because they have been concatenated as one 'word' - we would have to import and use regex, and part of the goal so
     far has been to solve problems with built-ins and their properties/structures/methods, and without lib imports.

     Fortunately - deliberately? - 'object' is also a member of, uniquely, the result string, so we use that instead.
'''
