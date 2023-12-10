import re

text_file = open("input-p1.txt", "r")
input = text_file.read()
text_file.close()

lines = input.splitlines()
total = 0

start_y = 0
start_x = 0
x_max = len(lines[0])
loop_map = {}

for l in range(len(lines)):
	line = lines[l]
	search = re.search('S', line)
	if search != None:
		start_y = l
		start_x = search.start()
		break

start = (start_x, start_y)
loop_map[start] = True

direction = 'down' # TODO calculate this

next_loc = start

steps = 0
while True:
	steps += 1
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
	count_left = 0
	polarity = ''
	corner_count = 0

	for t in range(len(line)):
		coords = (t, l)
		tile = line[t]
		prev_polarity = polarity

		if coords in loop_map:
			if tile == '-':
				continue
			if tile == '|':
				count_left += 1
				continue

			# tile in corners
			corner_count += 1
			polarity = 'up' if tile == 'J' or tile == 'L' else 'down'
			if prev_polarity == '':
				prev_polarity = polarity
			if polarity == prev_polarity:
				count_left += 1
			if corner_count % 2 == 0:
				polarity = ''
			continue


		if count_left % 2 == 1:
			possible_tiles[coords] = 1

def print_map():
	for l in range(len(lines)):
		line = lines[l]
		count_left = 0
		for t in range(len(line)):
			coords = (t, l)
			if coords in possible_tiles:
				lines[l] = lines[l][:t] + 'X' + lines[l][t + 1:]
			elif not coords in loop_map:
				lines[l] = lines[l][:t] + '.' + lines[l][t + 1:]

		print(lines[l])

size = sum(possible_tiles.values())
print(size)