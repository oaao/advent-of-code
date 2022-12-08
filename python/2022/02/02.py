"""
EXERCISE PROMPT: http://adventofcode.com/2022/day/2
"""

INPUT = (
    tuple(map(int, s.split(" ")))
    for s in
    open("input", mode="r", encoding="utf-8")
    .read()
    .strip("\n")
    .translate(str.maketrans("AXBYCZ", "112233"))
    .split("\n")
)
what_beats = {3: 1, 1: 2, 2: 3}

score = 0
for you, me in INPUT:
    score += me
    if what_beats[you] == me:
        score += 6
    elif you == me:
        score += 3

# part A solution
print(score)
