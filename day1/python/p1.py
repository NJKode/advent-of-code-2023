import re

text_file = open("input-p1.txt", "r")
input = text_file.read()
text_file.close()

total = 0

for line in input.splitlines():
	first_digit_search = re.search('\d', line)
	first_digit = first_digit_search.group(0)

	line_rev = line [::-1]
	last_digit_search = re.search('\d', line_rev)
	last_digit = last_digit_search.group(0)

	combined = int(first_digit + last_digit)
	total += combined

print (total)