"""
EXERCISE PROMPT: http://adventofcode.com/2019/day/5
"""

INPUT = [int(x.strip('\n')) for x in open('input.txt', mode='r', encoding='utf-8').readlines()]


def process_jumps(instrs, part='A'):

    jumps = instrs.copy()
    steps = 0

    i = 0

    while True:

        try:

            j = jumps[i]

            # negative index should count as a list exit
            # and would otherwise be index from back of list
            if i+j < 0:
                break
            else:
                # possibly trigger IndexError
                jumps[i+j]

            # adjust last instruction as per prompt
            if   part == 'A':
                jumps[i] += 1
            elif part == 'B':
                if j >= 3:
                    jumps[i] -= 1
                else:
                    jumps[i] += 1

            i = i+j

        except IndexError:
            break
        finally:
            steps += 1

    return steps


# part A solution:
print(f'A: {process_jumps(INPUT, part="A")}')

# part B solution:
print(f'B: {process_jumps(INPUT, part="B")}')
