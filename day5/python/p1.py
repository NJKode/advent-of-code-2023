import re

text_file = open("input-p1.txt", "r")
input = text_file.read()
text_file.close()

lines = input.split('\n')

seed_string = lines[0]

index = 0
parts = [[] for _ in range(7)]
for line in lines[3:999]:
	if line == '':
		continue
	elif re.match('^\d', line):
		parts[index].append(line)
	else:
		index += 1

lowest_location = -1

#seed_to_soil
seeds = seed_string.split(':')[1].split()
for seed_s in seeds:
	seed = int(seed_s)

	next_marker = seed
	for translations in parts:
		# translations[0] = seed_to_soil_lines

		for maps in translations:
			map_parts = maps.split()
			source_start = int(map_parts[1])

			if source_start > next_marker:
				continue

			map_range = int(map_parts[2])
			if next_marker > source_start + map_range:
				continue

			# within range
			destination_start = int(map_parts[0])
			map_diff = destination_start - source_start
			next_marker += map_diff
			break

	final_location = next_marker

	if lowest_location < 0 or final_location < lowest_location:
		lowest_location = final_location

print(lowest_location)

