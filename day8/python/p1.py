import re

text_file = open("input-p1.txt", "r")
input = text_file.read()
text_file.close()

lines = input.splitlines()

instructions = lines[0]

node_lines = lines[2::]
node_map = {}

for line in node_lines:
	parts = line.split(' = ')
	node = parts[0]

	next_nodes = re.findall(r'[A-Z]+', parts[1])
	node_map[node] = (next_nodes[0], next_nodes[1])

destination_reached = False
num_steps = 0
current_node = 'AAA'

while not destination_reached:
	for instruction in instructions:
		ind = 0 if instruction == 'L' else 1
		next_node = node_map[current_node][ind]
		num_steps += 1
		current_node = next_node
		if current_node == 'ZZZ':
			destination_reached = True
			break

print(num_steps)