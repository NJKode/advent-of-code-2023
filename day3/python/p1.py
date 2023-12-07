import re

text_file = open("input-p1.txt", "r")
input = text_file.read()
text_file.close()

lines = input.splitlines()


# store all symbol positions (x, y)
# run through numbers
sym_map = [[]] * len(lines)

# build up symbol sym_map
for l in range(len(lines)):
	sym_map[l] = []
	line = lines[l]
	symbols = re.finditer('[^\d|\.|\n]', line)
	for match in symbols:
		sym_map[l].append(match.start())

total = 0
for l in range(len(lines)):
	line = lines[l]
	max_width = len(line) - 1
	max_height = len(lines) - 1
	numbers = re.finditer('\d+', line)
	for match in numbers:
		start, end = match.span()
		num_size = end - start

		found = False

		# look left and right
		if start > 0:
			found = ((start - 1) in sym_map[l]) or (l > 0 and (start - 1) in sym_map[l - 1]) or (l < max_height and (start - 1) in sym_map[l + 1])

		if found == False and start < max_width:
			found = (end in sym_map[l]) or (l > 0 and end in sym_map[l-1]) or (l < max_height and end in sym_map[l + 1])

		# look above
		if found == False and l > 0:
			above_l = l - 1
			for ind in range(start, end):
				if ind in sym_map[above_l]:
					found = True
					break

		# look below
		if found == False and l < max_height:
			below_l = l + 1
			for ind in range(start, end):
				if ind in sym_map[below_l]:
					found = True
					break

		if found:
			num_string = match.group(0)
			total += int(num_string)


print(total)