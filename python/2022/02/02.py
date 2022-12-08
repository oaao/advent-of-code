"""
EXERCISE PROMPT: http://adventofcode.com/2022/day/2
"""

INPUT = tuple(open("input", mode="r", encoding="utf-8").read().strip("\n").split("\n"))
case_groups = (
    ("C X", "A Y", "B Z"),
    ("A X", "B Y", "C Z"),
    ("B X", "C Y", "A Z"),
)

# part A solution — case rows are win/tie/loss respectively
scoring = {
    # map(ord, ("X", "Y", "Z")) -> (88, 89, 90)
    case: n + ord(case[-1]) - 87
    for case_group, n in zip(case_groups, (6, 3, 0))
    for case in case_group
}
print(sum(map(lambda case: scoring[case], INPUT)))
