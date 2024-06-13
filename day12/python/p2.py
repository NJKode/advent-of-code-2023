import re
import functools
text_file = open("input-p1.txt", "r")
input = text_file.read()
text_file.close()

@functools.lru_cache
def combinations_in_slot(spring_groups: list[int], slot: str):
	slot_size = len(slot)
	spring_groups = tuple(spring_groups)
	min_size = sum(spring_groups) + len(spring_groups) - 1
	if min_size > slot_size:
		return 0
	if min_size == slot_size and '#' not in slot:
		return 1

	required = re.finditer(r'#', slot)
	required_list = list(required)
	if len(spring_groups) == 1:
		springs = spring_groups[0]
		if springs == slot_size:
			return 1

		if len(required_list) == 0:
			return slot_size - springs + 1

		if len(required_list) > springs:
			return 0

		start_index = required_list[0].start()
		end_index = required_list[-1].end()
		required_length = end_index - start_index
		if required_length > springs:
			return 0

		# TODO verify this!
		slot_end = min(start_index + springs, len(slot))
		slot_start = max(0, end_index - springs)

		return max(0, (slot_end - slot_start) - springs + 1)

	remaining_space = slot_size - min_size
	num_combinations = 0
	for s in range(remaining_space + 2):
		end_index = spring_groups[0] + s
		if slot[end_index] == '#':
			continue
		combo = combinations_in_slot((spring_groups[0]), slot[:end_index])
		if combo == 0:
			break
		remaining_springs = spring_groups[1::]
		num_combinations += combinations_in_slot(remaining_springs, slot[end_index+1::])
		if slot[s] == '#':
			break

	return num_combinations

@functools.lru_cache
def combinations_in_multiple_slots(springs: int, slots):
	slots = tuple(slots)
	valid_slot_indeces = [] # discard slots that are smaller than len springs
	required_slot_index = -1
	for s, slot in enumerate(slots):
		if len(slot) >= springs:
			valid_slot_indeces.append(s)
		if '#' in slot:
			if required_slot_index < 0:
				required_slot_index = s
			else:	# multiple required slots, impossible
				return 0

	if required_slot_index >= 0: # return combinations_in_multiple_slots for that slot
		return combinations_in_slot((springs), slots[required_slot_index])

	num_combos = 0
	for i in valid_slot_indeces: # simply sum combinations_in_multiple_slots per slot
		num_combos += combinations_in_slot((springs), slots[i])
	return num_combos

@functools.lru_cache
def arrange_spring_groups_in_slots(spring_groups: tuple[int], slots: tuple[str]):
	if len(spring_groups) == 0 or len(slots) == 0:
		return 0

	num_arrangements = 0
	first_slot = slots[0]
	slot_length = len(first_slot)

	if len(spring_groups) == 1:
		return combinations_in_multiple_slots(spring_groups[0], slots)
	if len(slots) == 1:
		return combinations_in_slot(spring_groups, slots[0])

	last_index = 0
	required_space = spring_groups[0]
	while required_space <= slot_length and last_index < len(spring_groups):
		last_index += 1
		if last_index < len(spring_groups) - 1:
			required_space += spring_groups[last_index] + 1

	 # the first spring group cannot fit in the first slot
	if last_index == 0:
		if '#' in first_slot:
			return 0
		else:
			return arrange_spring_groups_in_slots(spring_groups, slots[1::])

	for i in range(last_index, -1, -1):
		bunch = spring_groups[:i]
		combos = 0
		if len(bunch) > 0:
			combos = combinations_in_slot(bunch, first_slot)
			if combos == 0:
				continue
		if len(bunch) == 0 and '#' in first_slot:
			continue

		remaining_springs = spring_groups[i::]
		remaining_slots = slots[1::]

		complete = True
		if len(remaining_springs) == 0:
			for r_s in remaining_slots:
				if '#' in r_s:
					complete = False
					break
			if complete == True:
				num_arrangements += combos
			continue

		further_combos = arrange_spring_groups_in_slots(remaining_springs, remaining_slots)
		num_arrangements += max(combos, 1) * further_combos

	return num_arrangements


lines = input.splitlines()

total_num_arrangements = 0

def process_line(line: str):
	parts = line.split()
	nums_s = re.findall(r'\d+', parts[1])
	spring_groups = []
	for num_s in nums_s:
		spring_groups.append(int(num_s))
	spring_groups *= 5

	arrangement = ((parts[0] + '?') * 5)[:-1]
	slots = arrangement.split('.')
	slots = list(filter(None, slots)) # remove dupes

	num_arrangements = arrange_spring_groups_in_slots(tuple(spring_groups), tuple(slots))
	return num_arrangements

for line in lines:
	arrs = process_line(line)
	total_num_arrangements += arrs

print(total_num_arrangements)
