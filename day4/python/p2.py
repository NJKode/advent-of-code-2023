import re

text_file = open("input-p2.txt", "r")
input = text_file.read()
text_file.close()

lines = input.splitlines()
cards = []
score = 0

multipliers = [1] * len(lines)

for l in range(len(lines)):
	line = lines[l]
	card_score = 0
	card = line.split(':')[1].strip()
	parts = card.split('|')
	winning_numbers_s = parts[0].strip()
	nums = ' ' + parts[1].strip() + ' '

	winning_numbers = winning_numbers_s.split(' ')

	num_wins = 0
	for w_n in winning_numbers:
		w_n = w_n.strip()
		if len(w_n) == 0:
			continue
		if ' ' + w_n + ' ' in nums:
			num_wins += 1

	for w in range(num_wins):
		multipliers[l + w + 1] += multipliers[l]

for m in multipliers:
	score += m

print(score)