"""
EXERCISE PROMPT: http://adventofcode.com/2016/day/5
"""

import hashlib                                                        # rip the dream

INPUT = 'ojvtpuvg'
index = 0

pw_A = ''

li_B = list(' ' * 8)
el_B = list(range(8))                                                 # used to control first valid result per position

while True:

    h = hashlib.md5()
    h.update((INPUT + str(index)).encode('utf-8'))
    r = h.hexdigest()

    index += 1

    if r[:5] == '00000':
        # print('{} | iter {}'.format(r, index + 1))

        if len(pw_A) < 8:                                             # append to ptA pw until it is eight chars long
            pw_A += r[5]
            # print('A: {} appended'.format(r[5]))

        pos = int(r[5], 16)

        if pos in el_B:                                               # insert into ptB pw until no more valid positions
            li_B[pos] = r[6]
            el_B.remove(pos)
            # print('B: {} to pos {}'.format(r[6], r[5]))

    if len(pw_A) == 8 and len(el_B) == 0:
        pw_B = "".join(li_B)
        break


print(pw_A)                                                           # output Part A solution
print(pw_B)                                                           # output Part B solution
