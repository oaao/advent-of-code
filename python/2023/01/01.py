"""
EXERCISE PROMPT: http://adventofcode.com/2023/day/1
"""
import re
from typing import Dict, Generator, List


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
}
MAX_SUBSTRING_LENGTH = max((len(k)) for k in NUMWORD_MAP.keys())


def generate_calibration_values(lines: List[str]) -> Generator[str, None, None]:
    return map(
        int, (
            code[0] + code[-1]
            for code in (
                list(filter(str.isdigit, line)) for line in lines
            )
        )
    )


def replace_bounding_numwords(lines: List[str]) -> List[str]:
    """
    Make leftmost and rightmost valid number-word substitutions in a list of lines.

    The rightmost substitution reverses the line, as well as each numword string.
    This prevents errors such as "...oneight" resolving as "1ight" instead of "on8".
    """

    def replace_at_first_valid_number(line: str, mapping: Dict[str, str]) -> str:
        substring_slices = [
            line[idx:idx+MAX_SUBSTRING_LENGTH] for idx in range(len(line) - MAX_SUBSTRING_LENGTH + 1)
        ]
        for substring in substring_slices:
            # if we hit a number before a numword, use the original line
            if any((substring.startswith(num) for num in mapping.values())):
                break
            else:
                for word, num in mapping.items():
                    if substring.startswith(word):
                        return line.replace(word, num, 1)
        return line

    leftmost_subbed = (replace_at_first_valid_number(line, NUMWORD_MAP) for line in lines)
    rightmost_subbed = list(
        replace_at_first_valid_number(
            line[::-1], {k[::-1]: v for k, v in NUMWORD_MAP.items()}
        )[::-1]
        for line in leftmost_subbed
    )
    return rightmost_subbed


# part A solution
print(sum(generate_calibration_values(INPUT)))

# part B solution
print(sum(generate_calibration_values(replace_bounding_numwords(INPUT))))
