"""
EXERCISE PROMPT: http://adventofcode.com/2020/day/16
"""

def show(iterable):
	import pprint
	pprint.pprint(iterable, indent=2)


def parse_input(filename='input'):
	"""Parse input file into operable terms."""

	with open(filename, mode='r', encoding='utf-8') as f:
		lines = tuple(l.strip('\n') for l in f)

	endpts   = (0,) + tuple(n for i, ln in enumerate(lines) for n in (i, i+2) if ln == '') + (len(lines),)
	sections = (
		lines[i:j] for i, j in zip(endpts, endpts[1:])
	)

	rules, _, ticket, _, nearby_tickets = sections

	ticket, = ticket
	ticket  = tuple(int(s) for s in ticket.split(','))

	nearby_tickets = tuple(
		(
			i,
			tuple(int(s) for s in ln.split(','))
		)
		for i, ln in enumerate(nearby_tickets)
	)

	return rules, ticket, nearby_tickets


def parse_rules(rules):
	"""Parse rules strings into a ruleset dictionary."""

	ruleset = {}

	for rule in rules:

		# not a regex-friendly household
		s  = rule.replace(': ', ',').replace('-', ',').replace(' or ', ',').replace(' ', '_')
		ln = s.split(',')
		key, min1, max1, min2, max2 = ln

		ruleset[key] = (int(min1), int(max1)), (int(min2), int(max2))

	return ruleset


def reduce_ruleset_ranges(ruleset):
	"""Mathematically reduce ruleset ranges because I can guess what's coming..."""

	ranges        = tuple(tp for vals in ruleset.values() for tp in vals)
	sorted_by_low = sorted(ranges, key=lambda tp: tp[0])

	reduced = [sorted_by_low[0],]

	for pair in sorted_by_low[1:]:
		# we already sorted by first term, so
		# we are certain that smaller_pair[0] <= pair[0]
		smaller_pair = reduced[-1]
		if pair[0] <= smaller_pair[1]:
			higher_max   = max(pair[1], smaller_pair[1])
			reduced[-1] = (smaller_pair[0], higher_max)
			# print(f"Modified most recent range to: {(smaller_pair[0], higher_max)}")
		else:
			# print(f"Added: {pair}")
			reduced.append(pair)

	return reduced


def get_bad_tickets_and_values(ranges, tickets):

	bad_tickets = []

	for i, ticket in tickets:

		bad_values = []

		for n in ticket:
			if not any(lower <= n <= upper for lower, upper in ranges):
				bad_values.append(n)

		if bad_values:
			bad_tickets.append(
				(i, ticket, bad_values)
			)

	return bad_tickets


RULES, TICKET, NEARBY_TICKETS = parse_input()

# part A solution
ranges      = reduce_ruleset_ranges(parse_rules(RULES))
bad_tickets = get_bad_tickets_and_values(ranges, NEARBY_TICKETS)
print(sum((n for i, ticket, vals in bad_tickets for n in vals)))

# part B solution
