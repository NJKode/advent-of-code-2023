import re
import random
debug_mode = False
text_file = open("input-p1.txt", "r")
input = text_file.read()
text_file.close()

def call_combinations_in_slot(spring_groups: list[int], slot: str):
	if debug_mode: print(f'{spring_groups} in {slot}')
	result = combinations_in_slot(spring_groups, slot)
	if debug_mode: print(f'{spring_groups} in {slot} | {result}')
	return result

def combinations_in_slot(spring_groups: list[int], slot: str):
	slot_size = len(slot)
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
		combo = call_combinations_in_slot([spring_groups[0]], slot[:end_index])
		if combo == 0:
			break
		remaining_springs = spring_groups[1::]
		num_combinations += call_combinations_in_slot(remaining_springs, slot[end_index+1::])
		if slot[s] == '#':
			break


	return num_combinations

def call_combinations_in_multiple_slots(springs: int, slots: list[str]):
	if debug_mode: print(f'{springs} in {slots}')
	result = combinations_in_multiple_slots(springs, slots)
	if debug_mode: print(f'{springs} in {slots} | {result}')
	return result

def combinations_in_multiple_slots(springs: int, slots: list[str]):
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
		return call_combinations_in_slot([springs], slots[required_slot_index])

	num_combos = 0
	for i in valid_slot_indeces: # simply sum combinations_in_multiple_slots per slot
		num_combos += call_combinations_in_slot([springs], slots[i])

	return num_combos


def call_arrange_spring_groups_in_slots(spring_groups: list[int], slots: list[str]):
	if debug_mode: print(f'{spring_groups} in {slots}')
	result = arrange_spring_groups_in_slots(spring_groups, slots)
	if debug_mode: print(f'{spring_groups} in {slots} | {result}')
	return result

def arrange_spring_groups_in_slots(spring_groups: list[int], slots: list[str]):
	if len(spring_groups) == 0 or len(slots) == 0:
		return 0

	num_arrangements = 0
	first_slot = slots[0]
	slot_length = len(first_slot)

	if len(spring_groups) == 1:
		return call_combinations_in_multiple_slots(spring_groups[0], slots)
	if len(slots) == 1:
		return call_combinations_in_slot(spring_groups, slots[0])

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
			return call_arrange_spring_groups_in_slots(spring_groups, slots[1::])

	for i in range(last_index, -1, -1):
		bunch = spring_groups[:i]
		combos = 0
		if len(bunch) > 0:
			combos = call_combinations_in_slot(bunch, first_slot)
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


		further_combos = call_arrange_spring_groups_in_slots(remaining_springs, remaining_slots)
		num_arrangements += max(combos, 1) * further_combos

	return num_arrangements


lines = input.splitlines()

total_num_arrangements = 0

def process_line(line: str):
	parts = line.split()
	arrangement = parts[0]
	nums_s = re.findall(r'\d+', parts[1])
	spring_groups = []
	for num_s in nums_s:
		spring_groups.append(int(num_s))

	slots = arrangement.split('.')
	slots = list(filter(None, slots))

	num_arrangements = call_arrange_spring_groups_in_slots(spring_groups, slots)
	print(f'{line} | {num_arrangements}')
	return num_arrangements


test = random.randrange(0, len(lines))
# process_line(lines[test])
for line in lines:
	arrs = process_line(line)
	total_num_arrangements += arrs


answer = 7716
print(total_num_arrangements)
if answer == total_num_arrangements:
	print('Succeeded!')
else:
	print('Failed. Required:', answer)