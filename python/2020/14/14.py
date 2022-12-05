"""
EXERCISE PROMPT: http://adventofcode.com/2020/day/14
"""

INPUT = [x.strip('\n') for x in open('input', mode='r', encoding='utf-8')]


def process_input(declarations):

    instr = []
    batch = {'mask': (), 'writes' = []}

    for decl in declarations:
        if 'mask' in decl:
            instr.append(batch)
            batch = {'mask': None, 'writes': []}
            batch["mask"] = list((i, int(c)) for i, c in enumerate(reversed(decl.strip('mask = '))) if c != 'X')
        else:
            write = tuple(decl.strip('mem[').split('] = '))
            batch["writes"].append(write)

    return instr


    

# reverse() the mask and use its enum as the exponent?


def show(it):
    import pprint
    pprint.pprint(it, indent=2)

show(process_input(INPUT))
