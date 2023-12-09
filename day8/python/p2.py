import re
import math

text_file = open("input-p2.txt", "r")
input = text_file.read()
text_file.close()

lines = input.splitlines()

instructions = lines[0]

node_lines = lines[2::]
node_map = {}
starting_nodes = []

for line in node_lines:
	parts = line.split(' = ')
	node = parts[0]
	if node.endswith('A'):
		starting_nodes.append(node)

	next_nodes = re.findall(r'[A-Z]+', parts[1])
	node_map[node] = (next_nodes[0], next_nodes[1])

map_modulos = []

for c in range(len(starting_nodes)):
	current_node = starting_nodes[c]
	times_traversed = 0
	num_steps = 0

	while times_traversed <= 2:
		for instruction in instructions:
			ind = 0 if instruction == 'L' else 1
			next_node = node_map[current_node][ind]
			num_steps += 1
			current_node = next_node
			if current_node.endswith('Z'):
				times_traversed += 1
				if times_traversed == 1:
					map_modulos.append((num_steps, 0))
				elif times_traversed == 2:
					prev, _ = map_modulos[c]
					map_modulos[c] = (prev, num_steps - prev)
					break

steps_per_loop = []

for mod in map_modulos:
	steps_per_loop.append(mod[0])

lcm = math.lcm(*steps_per_loop)
print(lcm)