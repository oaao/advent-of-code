"""
EXERCISE PROMPT: http://adventofcode.com/2023/day/1
"""
import itertools
import operator
import re
from typing import Generator, List


INPUT = [s.strip("\n") for s in open("input", mode="r", encoding="utf-8")]

NUMWORD_MAP = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
} | {n: n for n in map(str, range(1, 10))}

PATTERN = r'(?=('+'zero|one|two|three|four|five|six|seven|eight|nine|[0-9]))'


def generate_calibration_values(
    lines: List[str], convert_numwords: bool = False
) -> Generator[int, None, None]:

    first_and_last = operator.itemgetter(*[0,-1])

    if not convert_numwords:
        subfunction = (
            first_and_last,
            map(re.sub, itertools.cycle(['\D']), itertools.cycle(['']), lines)
        )
    else:
        subfunction = (
            map, itertools.cycle([NUMWORD_MAP.get]),
            list(map(
                first_and_last,
                map(re.findall, itertools.cycle([PATTERN]), INPUT)
            ))
        )

    return map(
        int, map(
            ''.join,
            map(
                *subfunction
            )
        )
    )


# part A solution
print(sum(generate_calibration_values(INPUT)))

# part B solution
print(sum(generate_calibration_values(INPUT, convert_numwords=True)))

