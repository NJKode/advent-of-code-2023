text_file = open("input-p1.txt", "r")
input = text_file.read()
text_file.close()

lines = input.splitlines()

start = (0, 0)
loopmap = {start: True}
corner_map = {}
current_pos = start

minX = 0
maxX = 0
minY = 0
maxY = 0

prev_corner = ''
for line in reversed(lines):
	parts = line.split()
	direction = parts[0]
	length = int(parts[1])

	if direction == 'U' or direction == 'D':
		corner_map[current_pos] = direction
		prev_corner = direction
	else:
		corner_map[current_pos] = 'D' if prev_corner == 'U' else 'U'

	for d in range(length):
		x, y = current_pos
		if direction == 'R':
			current_pos = (x + 1, y)
		elif direction == 'L':
			current_pos = (x - 1, y)
		elif direction == 'U':
			current_pos = (x, y - 1)
		elif direction == 'D':
			current_pos = (x, y + 1)
		loopmap[current_pos] = True

		minX = min(minX, current_pos[0])
		maxX = max(maxX, current_pos[0])
		minY = min(minY, current_pos[1])
		maxY = max(maxY, current_pos[1])



area = 0

for y in range(minY, maxY + 1):
	line = ''
	edge_count = 0
	corner_count = 0
	polarity = ''
	for x in range(minX, maxX + 1):
		prev_polarity = polarity
		if (x,y) in loopmap:
			line += '#'
			if (x - 1, y) not in loopmap or (x + 1, y) not in loopmap:
				edge_count += 1

			area += 1
			if (x, y) in corner_map:
				corner_count += 1
				polarity = corner_map[(x, y)]
				if prev_polarity == '':
					prev_polarity = polarity
				if polarity == prev_polarity:
					edge_count += 1
				if corner_count % 2 == 0:
					polarity = ''
		elif edge_count % 2 == 1:
			area += 1
			line += '#'
		else:
			line += '.'
	# print(line)

print(area)

# a: 47675