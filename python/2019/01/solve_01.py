"""
EXERCISE PROMPT: http://adventofcode.com/2019/day/1
"""

INPUT = [int(n.strip('\n')) for n in open('input.txt', mode='r', encoding='utf-8')]


def fuel_per_mass(m):
    # int(float) always rounds down, while round(float) rounds to nearest int
    return int(m / 3) -2


def recursive_fuel_total(masses):

    recursive_masses = []

    for m in masses:

        while m > 0:

            m = fuel_per_mass(m)

            if m > 0:
                recursive_masses.append(m)

    return recursive_masses


# part A solution
print(f'A: {sum(fuel_per_mass(m) for m in INPUT)}')

# part B solution
print(f'B: {sum(recursive_fuel_total(INPUT))}')
