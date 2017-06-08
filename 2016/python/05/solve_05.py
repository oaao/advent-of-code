"""
EXERCISE PROMPT: http://adventofcode.com/2016/day/5
"""

import hashlib                                                        # rip the dream

INPUT = 'ojvtpuvg'
index = 0

pw    = ''

while len(pw) < 8:

    h = hashlib.md5()
    h.update((INPUT + str(index)).encode('utf-8'))
    r = h.hexdigest()

    index += 1

    if r[:5] == '00000':
        pw += r[5]
        # print('{} found on iteration {}'.format(r, index+1))

print(pw)
