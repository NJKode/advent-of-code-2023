text_file = open("input-p1.txt", "r")
input = text_file.read()
text_file.close()

def transpose_lines(lines):
	lines_t = []
	for c in range(len(lines[0])):
		line = []
		for y in range(len(lines)):
			line.insert(0, (lines[y][c]))
		lines_t.append(line)
	return lines_t

# REMEBER TO GO RIGHT
platform = transpose_lines(list(input.splitlines()))
moved = []
total_load = 0

for column in platform:
	c_b = column.copy()
	last_empty_space = len(column) - 1
	for c in range(len(column) - 1, -1, -1):
		item = column[c]
		if item == '.':
			continue

		if item == 'O':
			item_at_empty_space = column[last_empty_space]
			column[last_empty_space] = 'O'
			column[c] = item_at_empty_space
			last_empty_space -= 1

		if item == '#':
			last_empty_space = c - 1

	# print(f'{c_b} -> {column}')
	load = 0
	for c in range(len(column)):
		if column[c] == 'O':
			load += c + 1

	total_load += load

print(total_load)

