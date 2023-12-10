text_file = open("input-p1.txt", "r")
input = text_file.read()
text_file.close()

lines = input.splitlines()

start_y = 0
start_x = 0
loop_map = {}

for l in range(len(lines)):
	line = lines[l]
	if 'S' in line:
		start_y = l
		start_x = line.index('S')
		break

start = (start_x, start_y)
loop_map[start] = True
direction = 'down' # TODO calculate this
next_loc = start

while True:
	if direction == 'up':
		next_loc = (next_loc[0], next_loc[1] - 1)
	elif direction == 'down':
		next_loc = (next_loc[0], next_loc[1] + 1)
	elif direction == 'left':
		next_loc = (next_loc[0] - 1, next_loc[1])
	elif direction == 'right':
		next_loc = (next_loc[0] + 1, next_loc[1])

	if next_loc == start:
		break

	loop_map[next_loc] = True

	next_pipe = lines[next_loc[1]][next_loc[0]]

	if next_pipe == '-' or next_pipe == '|':
		direction = direction
	elif direction == 'right':
		direction = 'down' if next_pipe == '7' else 'up'
	elif direction == 'left':
		direction = 'down' if next_pipe == 'F' else 'up'
	elif direction == 'up':
		direction = 'right' if next_pipe == 'F' else 'left'
	elif direction == 'down':
		direction = 'right' if next_pipe == 'L' else 'left'

possible_tiles = {}
for l in range(len(lines)):
	line = lines[l]
	edge_count = 0
	polarity = ''
	corner_count = 0

	for t in range(len(line)):
		coords = (t, l)
		prev_polarity = polarity

		if coords in loop_map:
			tile = line[t]
			if tile == '-':
				continue
			if tile == '|':
				edge_count += 1
				continue

			# tile in corners
			corner_count += 1
			polarity = 'up' if tile == 'J' or tile == 'L' else 'down'
			if prev_polarity == '':
				prev_polarity = polarity
			if polarity == prev_polarity:
				edge_count += 1
			if corner_count % 2 == 0:
				polarity = ''
			continue


		if edge_count % 2 == 1:
			possible_tiles[coords] = 1

def print_map():
	for l in range(len(lines)):
		line = lines[l]
		for t in range(len(line)):
			coords = (t, l)
			if coords in possible_tiles:
				lines[l] = lines[l][:t] + 'X' + lines[l][t + 1:]
			elif not coords in loop_map:
				lines[l] = lines[l][:t] + '.' + lines[l][t + 1:]

		print(lines[l])

size = sum(possible_tiles.values())
print(size)