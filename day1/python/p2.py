import re

text_file = open("input-p2.txt", "r")
input = text_file.read()
text_file.close()

numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

total = 0

lines = input.splitlines()

for l in range(len(lines)):
	line = lines[l]
	first_digit_search = re.search('\d', line)
	first_digit = ''
	first_digit_pos = -1
	if (first_digit_search != None):
		first_digit = first_digit_search.group(0)
		first_digit_pos = first_digit_search.start()

	if first_digit_pos != 0:
		number_pos = -1
		first_number = ''
		for n in range(len(numbers)):
			test_num = numbers[n]
			pos = line.find(test_num)

			if pos >= 0 and (pos < number_pos or number_pos < 0):
				number_pos = pos
				first_number = str(n)

		if first_digit_pos < 0 or (number_pos >= 0 and number_pos < first_digit_pos):
			first_digit = first_number

	line_rev = line [::-1]
	last_digit_search = re.search('\d', line_rev)
	last_digit = ''
	last_digit_pos = -1

	if (last_digit_search != None):
		last_digit = last_digit_search.group(0)
		last_digit_pos = last_digit_search.start()


	if last_digit_pos != 0:
		number_pos = -1
		last_number = ''
		for n in range(len(numbers)):
			test_num = numbers[n] [::-1]
			pos = line_rev.find(test_num)

			if pos >= 0 and (pos < number_pos or number_pos < 0):
				number_pos = pos
				last_number = str(n)

		if last_digit_pos < 0 or (number_pos >= 0 and number_pos < last_digit_pos):
			last_digit = last_number


	combined = int(first_digit + last_digit)
	total += combined

print (total)