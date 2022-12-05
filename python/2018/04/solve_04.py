"""
EXERCISE PROMPT: http://adventofcode.com/2018/day/4
"""

import re#ally?????????

from collections import Counter
from functools import reduce

INPUT = [
    re.split(
        r'\W+',
        s[1:].strip('\n')
    )
    for s in open('input.txt', mode='r', encoding='UTF-8')
]


def generate_timestamp(l):
    return reduce((lambda x, y: str(x) + str(y)), l[:5])


def format_logs(logs):

    formatted = []

    for l in logs:

        l[5]  = int(l[6]) if l[5] == 'Guard' else l[5]
        l[:5] = map(lambda x: int(x), l[:5])

        formatted.append(l[:6])

    return formatted


def get_minutes_asleep(logs):

    current_guard = None
    sleep_at      = None
    wake_at       = None

    guard_minutes = dict(
        (l[5], Counter())
        for l in logs
        if isinstance(l[5], int)
    )

    for l in logs:

        if isinstance(l[5], int):
            current_guard = l[5]

        elif l[5] == 'falls':
            sleep_at = l[4]

        elif l[5] == 'wakes':

            wake_at = l[4]

            for minute in range(sleep_at, wake_at):

                guard_minutes[current_guard][minute] += 1

    return guard_minutes


logs_sorted = sorted(INPUT, key=generate_timestamp)
logs        = format_logs(logs_sorted)

# solve part A
minutes_asleep = get_minutes_asleep(logs)
laziest_guard  = sorted(
    [
        (guard, sum(minutes.values()))
        for guard, minutes in minutes_asleep.items()
    ],
    key=lambda x: x[1],
    reverse=True
)[0][0]

laziest_guard_minute = minutes_asleep[laziest_guard].most_common(1)[0][0]


# solve part B
# piping Counter() objects combines them, taking the max value for common keys
absolute_laziest_minute = reduce(
    (lambda x, y: x | y),
    minutes_asleep.values()
).most_common(1)[0][0]

most_reliable_sleeper = sorted(
    [
        (guard, minutes[absolute_laziest_minute])
        for guard, minutes in minutes_asleep.items()
    ],
    key=lambda x: x[1],
    reverse=True
)[0][0]


print(f'A: {laziest_guard * laziest_guard_minute}')
print(f'B: {most_reliable_sleeper * absolute_laziest_minute}')
