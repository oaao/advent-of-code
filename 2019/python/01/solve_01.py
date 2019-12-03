"""
EXERCISE PROMPT: http://adventofcode.com/2019/day/1
"""

INPUT = [int(n.strip('\n')) for n in open('input.txt', mode='r', encoding='utf-8')]


def get_fuel_costs(masses):
    # int(float) always rounds down, while round(float) rounds to nearest int
    return (int(m / 3) - 2 for m in masses)


# part A solution
print(f'A: {sum(get_fuel_costs(INPUT))}')