text_file = open("input-p1.txt", "r")
input = text_file.read()
text_file.close()

parts = input.split('\n\n')

raw_workflows = parts[0].splitlines()
raw_ratings = parts[1].splitlines()
workflows = {}

for wf in raw_workflows:
	parts = wf.split('{')
	name = parts[0]
	raw_rules = parts[1][:-1].split(',')
	rule = ('a', '>', 12345, 'A')
	rules = []
	for rr in raw_rules:
		if ':' not in rr:
			rules.append(('flow', rr))
			continue

		func = rr.split(':')
		then = func[1]

		operation = '>' if '>' in func[0] else '<'
		operands = func[0].split(operation)
		val = int(operands[1])
		cat = operands[0]

		rules.append(('rule', (cat, operation, val, then)))
	workflows[name] = rules

parts = []
for raw_part in raw_ratings:
	categories = raw_part[1:-1].split(',')
	part = {}
	for cat in categories:
		vals = cat.split('=')
		part[vals[0]] = int(vals[1])
	parts.append(part)


sum_ratings = 0
for part in parts:
	op = 'in'
	while op != 'A' and op != 'R':
		# print(op, end=' -> ')
		rules = workflows[op]
		for rule in rules:
			kind, operation = rule
			if kind == 'flow':
				op = operation
				break
			cat, comp, val, then = operation
			if comp == '<' and part[cat] < val:
				op = then
				break
			elif comp == '>' and part[cat] > val:
				op = then
				break

	# print(op)
	if op == 'A':
		part_rating = sum(part.values())
		sum_ratings += part_rating

print(sum_ratings)