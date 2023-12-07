import re

text_file = open("input-p1.txt", "r")
input = text_file.read()
text_file.close()

lines = input.splitlines()

time_parts = lines[0].split(':')[1]
time_a = time_parts.split()
time_s = ''
for t in time_a:
	time_s += t
time = int(time_s)

record_parts = lines[1].split(':')[1]
record_a = record_parts.split()
record_s = ''
for r in record_a:
	record_s += r
record = int(record_s)

print(time, record)

stuff = []

winning_ways = 0

for charge_time in range(time):
	speed = charge_time
	time_left = time - charge_time
	distance = time_left * speed

	if distance > record:
		winning_ways += 1



print(winning_ways)
