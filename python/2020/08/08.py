"""
EXERCISE PROMPT: http://adventofcode.com/2020/day/8
"""

from typing import List, Tuple


INPUT = [
	instr.strip('\n').split(' ')
	for instr in open('input', mode='r', encoding='utf-8')
]


def execute_instructions(
	instr_list: List[Tuple[str, int]],
	debug: bool =False
) -> int:

	history = set()
	acc_val = 0
	_index  = 0

	# finding the index of an element in a list is slower
	# than starting with index tracking in the first place
	while _index < len(instr_list):

		# accommodate parts A and B
		if _index in history:
			if debug:
				return None
			else:
				return acc_val 

		history.add(_index)

		opcode, n = instr_list[_index]

		if   opcode == 'acc':
			acc_val += n
			_index += 1
		elif opcode == 'jmp':
			_index += n
		else:
			_index += 1

	return acc_val


def debug_instructions(instr_list: List[Tuple[str, int]]) -> int:

	for _index in range(len(instr_list)):

		if   instr_list[_index][0] == 'acc':
			continue
		elif instr_list[_index][0] == 'jmp':
			_opcode = 'nop'
		elif instr_list[_index][0] == 'nop':
			_opcode = 'jmp'

		# easiest is to just slap the new opcode at the end and keep going
		new_instr = (_opcode, instr_list[_index][1])
		_instr_list = instr_list[:_index] + [new_instr,] + instr_list[_index+1:]

		acc_val = execute_instructions(_instr_list, debug=True)

		if acc_val is not None:
			return acc_val


instructions = [(opcode, int(n)) for opcode, n in INPUT]

# part A solution
print(execute_instructions(instructions))

# part B solution
print(debug_instructions(instructions))
