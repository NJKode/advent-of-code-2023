text_file = open("input-p1.txt", "r")
input = text_file.read()
text_file.close()

grid = []

lines = input.splitlines()

for line in lines:
	grid.append(list(line))

grid_width = len(lines[0])
grid_height = len(lines)

def move(x, y, d):
	next_pos = ()
	if d == 'r':
		next_pos = (x + 1, y, d)
	elif d == 'l':
		next_pos = (x - 1, y, d)
	elif d == 'u':
		next_pos = (x, y - 1, d)
	elif d == 'd':
		next_pos = (x, y + 1, d)
	return next_pos

def split(x, y, d):
	next_pos = []
	if d == 'l' or d  == 'r':
		up = move(x, y, 'u')
		down = move(x, y, 'd')
		next_pos += [up, down]
	elif d == 'u' or d == 'd':
		left = move(x, y, 'l')
		right = move(x, y, 'r')
		next_pos += [left, right]
	return next_pos

reflect_left = { 'u': 'l', 'l': 'd', 'd': 'r', 'r': 'u' }
reflect_right = { 'u': 'r', 'r': 'd', 'd': 'l', 'l': 'u'}
def reflect(x, y, d, m):
	new_d = ''
	if m == '/':
		if d == 'u' or d == 'd':
			new_d = reflect_right[d]
		elif d == 'l' or d == 'r':
			new_d = reflect_left[d]
	if m == '\\':
		if d == 'u' or d == 'd':
			new_d = reflect_left[d]
		elif d == 'l' or d == 'r':
			new_d = reflect_right[d]

	return move(x, y, new_d)

start_tiles = []
for x in range(grid_width):
	start_tiles.append((x, 0, 'd'))
	start_tiles.append((x, grid_width - 1, 'u'))
for y in range(grid_height):
	start_tiles.append((0, y, 'r'))
	start_tiles.append((grid_height - 1, y, 'l'))

max_energy = 0
for start in start_tiles:
	beam_ends = [start]
	beams_travelling = True
	energized = { (start[0], start[1]): True }
	tracker = { start: True }
	while len(beam_ends) > 0:
		x, y, d = beam_ends.pop()
		current_tile = grid[y][x]
		next_tiles = []

		if current_tile == '.':
			next_tiles.append(move(x, y, d))
		elif current_tile == '|':
			if d == 'r' or d == 'l':
				next_tiles += split(x, y, d)
			elif d == 'u' or d == 'd':
				next_tiles.append(move(x, y, d))

		if current_tile == '-':
			if d == 'r' or d == 'l':
				next_tiles.append(move(x, y, d))
			elif d == 'u' or d == 'd':
				next_tiles += split(x, y, d)

		if current_tile == '/' or current_tile == '\\':
			next_tiles.append(reflect(x, y, d, current_tile))

		for tile in next_tiles:
			x, y, d = tile
			if x < grid_width and x >= 0 and y < grid_height and y >= 0:
				if tile not in tracker:
					beam_ends.append(tile)
					tracker[tile] = True
					energized[(x, y)] = True

	max_energy = max(max_energy, len(energized))

print(max_energy)
