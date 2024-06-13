import bisect
text_file = open("input-p1-test.txt", "r")
input = text_file.read()
text_file.close()

lines = input.splitlines()
map_width = len(lines[0])
map_height = len(lines)

start = (0, 0)
for y in range(len(lines)):
	if 'S' in lines[y]:
		x = lines[y].index('S')
		start = (x, y)

def get_next_nodes(current_node, score):
	valid_next_nodes = []

	x, y = current_node
	if x > 0 and lines[y][x - 1] == '.':
		valid_next_nodes.append(((x - 1, y), score + 1))
	if x < map_width - 1 and lines[y][x + 1] == '.':
		valid_next_nodes.append(((x + 1, y), score + 1))
	if y > 0 and lines[y - 1][x] == '.':
		valid_next_nodes.append(((x, y - 1), score + 1))
	if y < map_height - 1 and lines[y + 1][x] == '.':
		valid_next_nodes.append(((x, y + 1), score + 1))

	return valid_next_nodes

def get_next_nodes_inf(current_node, score):
	valid_next_nodes = []

	x, y = current_node
	l = (x - 1) % map_width
	r = (x + 1) % map_width
	u = (y - 1) % map_height
	d = (y + 1) % map_height

	if lines[y % map_height][l] == '.':
		valid_next_nodes.append(((x - 1, y), score + 1))
	if lines[y % map_height][r] == '.':
		valid_next_nodes.append(((x + 1, y), score + 1))
	if lines[u][x % map_width] == '.':
		valid_next_nodes.append(((x, y - 1), score + 1))
	if  lines[d][x % map_width] == '.':
		valid_next_nodes.append(((x, y + 1), score + 1))

	return valid_next_nodes


open_list = [((start), 0)]
closed_list = {}

visited_map = { start: 0 }

current_coords = start
steps = 10

while len(open_list) != 0:
	current_coords, score = open_list.pop()

	closed_list[current_coords] = score
	neighbours = get_next_nodes(current_coords, score)
	for neighbor in neighbours:
		n_coords, n_score = neighbor
		if n_coords in closed_list:
			continue

		if n_coords not in visited_map:
			visited_map[neighbor[0]] = neighbor[1]
			bisect.insort(open_list, neighbor, key=lambda r: r[1] * -1)
		else:
			dist = visited_map[neighbor[0]]
			if n_score < dist:
				visited_map[n_coords] = n_score
				node_in_open = [(i, node) for (i, node) in enumerate(open_list) if node[0] == neighbor[0]]
				index, _ = node_in_open[0]
				open_list = open_list[:index] + open_list[(index + 1)::]
				bisect.insort(open_list, neighbor, key=lambda r: r[1] * -1)


valid = 0
for coords, score in closed_list.items():
	if score % 2 == 0:
		valid += 1

# print(valid)
print(len(closed_list))

dumb_count = 0
for line in lines:
	for c in line:
		if c == '.' or c == 'S':
			dumb_count += 1

print(dumb_count)