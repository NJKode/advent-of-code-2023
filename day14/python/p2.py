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

cycles = 1_000_000_00
directions = 4
# REMEBER TO GO RIGHT
platform = transpose_lines(list(input.splitlines()))
moved = []
total_load = 0

platform_before = platform.copy()
hash_map = {}
remainder = -1
cycle_length = -1
for cycle in range(cycles):
	key = ''
	for direction in range(directions):
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
			if direction == directions - 1:
				key += ''.join(column)
			# print(f'{c_b} -> {column}')

		platform = transpose_lines(platform)

	if remainder == -1 and key in hash_map:
		print('cycle found')
		cycle_start = hash_map[key]
		cycle_length = cycle - cycle_start
		remainder = (cycles - cycle_start - 1) % (cycle_length)
	else:
		hash_map[key] = cycle

	if remainder == 0:
		for column in platform:
			load = 0
			for c in range(len(column)):
				if column[c] == 'O':
					load += c + 1

			total_load += load
		break
	elif remainder > 0:
		remainder -= 1
		continue

print(total_load)
