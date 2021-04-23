"""
EXERCISE PROMPT: http://adventofcode.com/2020/day/16
"""


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
		(i, tuple(int(s) for s in ln.split(',')))
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


# as it turns out, this was completely unnecessary. nice
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
			# print(f"Added: {pair} as most recent range")
			reduced.append(pair)

	return reduced


def get_invalid_tickets_and_values(ranges, tickets):
	"""Get an enumerated list of bad tickets and invalid values within each."""

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


def get_valid_tickets(tickets, rules):
	"""Get a filtered list of only tickets with no invalid values."""

	ranges  = reduce_ruleset_ranges(parse_rules(rules))
	bad_ids = {i for i, _, _ in get_invalid_tickets_and_values(ranges, tickets)}

	filtered = tuple(t for i, t in tickets if i not in bad_ids)

	return filtered


def match_possible_ticket_rows(tickets, rules):
	"""Determine which ticket columns *can* match which fields."""

	tickets = get_valid_tickets(tickets, rules)
	ruleset = parse_rules(rules)

	inverse    = tuple(zip(*tickets))
	candidates = list(ruleset.keys()) # need mutability; we gon be poppin'
	matches    = {cand: [] for cand in candidates}

	# forgive me
	for i, column in enumerate(inverse):
		for cand in candidates:
			if all(any(lower <= n <= upper for lower, upper in ruleset[cand]) for n in column):
				matches[cand].append(i)

	return matches


def match_exact_ticket_rows(tickets, rules):

	possible = match_possible_ticket_rows(tickets, rules)
	exact    = {}

	while possible:
		# sort by list length so we can just work in sequence:
		for k, v in sorted(possible.items(), key=lambda d: len(d[1])):
			if len(v) == 1:
				n, = possible.pop(k, None)
				exact[k] = n
				for _, values in possible.items():
					values.remove(n)

	return exact


RULES, TICKET, NEARBY_TICKETS = parse_input()

# part A solution
ranges = reduce_ruleset_ranges(parse_rules(RULES))
print(sum((n for i, tk, vals in get_invalid_tickets_and_values(ranges, NEARBY_TICKETS) for n in vals)))

# part B solution
from functools import reduce
print(
	reduce(
		lambda x, y: x * y,
		{TICKET[v] for k, v in match_exact_ticket_rows(NEARBY_TICKETS, RULES).items() if k.startswith('departure')}
	)
)
