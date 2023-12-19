import bisect
import math
text_file = open("input-p1.txt", "r")
input = text_file.read()
text_file.close()

lines = input.splitlines()
map_width = len(lines[0])
map_height = len(lines)
destination = (map_width - 1, map_height - 1)

type Position = tuple(int, int, str, int)
type Score = tuple(int, int, int)
type Node = (Position, Score)
type Coords = (int, int)

def distance_to_end(coords) -> int:
	x, y = coords
	return abs(destination[0] - x) + abs(destination[1] - y)

def heuristic(coords):
	return distance_to_end(coords)

def get_valid_next_nodes(current_node: Position, scores) -> list[Node]:
	x, y, direction, run = current_node
	f, g, h = scores
	new_coords = {}

	if direction == '':
		new_coords = {
			'r': (x + 1, y),
			'd': (x, y + 1)
		}
	elif run < 4:
		if direction == 'l' and x - 1 >= 0:
			new_coords['l'] = (x - 1, y)
		elif (direction == 'r') and x + 1 < map_width:
			new_coords['r'] = (x + 1, y)
		elif (direction == 'd') and y + 1 < map_height:
			new_coords['d'] = (x, y + 1)
		elif direction == 'u' and y - 1 >= 0:
			new_coords['u'] = (x, y - 1)
	else:
		new_coords = {
			'l': (x - 1, y),
			'r': (x + 1, y),
			'u': (x, y - 1),
			'd': (x, y + 1)
		}

		if direction == 'r' or x - 1 < 0 or (direction == 'l' and run >= 10) or ((direction == 'u' or direction == 'd') and x - 4 < 0):
			new_coords.pop('l', None)
		if direction == 'l' or x + 1 >= map_width or (direction == 'r' and run >= 10) or ((direction == 'u' or direction == 'd') and x + 4 >= map_width):
			new_coords.pop('r', None)
		if direction == 'u' or y + 1 >= map_height or (direction == 'd' and run >= 10) or ((direction == 'l' or direction == 'r') and y + 4 >= map_height):
			new_coords.pop('d', None)
		if direction == 'd' or y - 1 < 0 or (direction == 'u' and run >= 10) or ((direction == 'l' or direction == 'r') and y - 4 < 0):
			new_coords.pop('u', None)

	valid_next_nodes = []
	for dir, coords in new_coords.items():
		new_x, new_y = coords
		new_run = run + 1 if dir == direction or direction == '' else 1
		next_h = heuristic(coords)
		next_g = g + int(lines[new_y][new_x])
		next_f = next_g + next_h
		valid_next_nodes.append(((new_x, new_y, dir, new_run), (next_f, next_g, next_h )))
	return valid_next_nodes

start = (0, 0, '', 0)
start_g = 0
start_h = heuristic((0,0))
start_f = start_g + start_h
open_list: list[Node] = [((start), (start_f, start_g, start_h))]
closed_list = {}
visited_map = { start: 0 }

current_node = start
current_coords = current_node[:2]
final_score = 0

parent_map = {}
final_node = ()

while len(open_list) != 0:
	current_node, score = open_list.pop()
	current_coords: Coords = current_node[:2]
	if current_coords == destination:
		final_score = score[1]
		final_node = current_node
		break

	closed_list[current_node] = True
	neighbours = get_valid_next_nodes(current_node, score)
	for neighbor in neighbours:
		if neighbor[0] in closed_list:
			continue

		if neighbor[0] not in visited_map:
			parent_map[neighbor[0]] = current_node
			visited_map[neighbor[0]] = neighbor[1][1]
			bisect.insort(open_list, neighbor, key=lambda r: r[1][0] * -1)
		else:
			existing_g = visited_map[neighbor[0]]
			f, g, h = neighbor[1]
			if g < existing_g:
				parent_map[neighbor[0]] = current_node
				visited_map[neighbor[0]] = g
				node_in_open = [(i, node) for (i, node) in enumerate(open_list) if node[0] == neighbor[0]]
				index, _ = node_in_open[0]
				open_list = open_list[:index] + open_list[(index + 1)::]
				bisect.insort(open_list, neighbor, key=lambda r: r[1][0] * -1)

print(final_score)

# traverse_node = final_node
# traverse_list = [final_node]

# while traverse_node[:2] != (0, 0):
# 	traverse_node = parent_map[traverse_node]
# 	traverse_list.append(traverse_node)
# for node in reversed(traverse_list):
# 	print(node[:2], end=" -> ")