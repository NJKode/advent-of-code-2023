import re

text_file = open("input-p1.txt", "r")
input = text_file.read()
text_file.close()

lines = input.splitlines()

times = lines[0].split()[1:]
records = lines[1].split()[1:]

stuff = []

for race_index in range(len(times)):
	winning_ways = 0

	time_allowed = int(times[race_index])
	race_record = int(records[race_index])

	for charge_time in range(time_allowed):
		speed = charge_time
		time_left = time_allowed - charge_time
		distance = time_left * speed

		if distance > race_record:
			winning_ways += 1

	stuff.append(winning_ways)

score = 1

for s in stuff:
	score *= s

print(score)
