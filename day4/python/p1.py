import re

text_file = open("input-p1.txt", "r")
input = text_file.read()
text_file.close()

lines = input.splitlines()
cards = []
score = 0
for line in lines:
	card_score = 0
	card = line.split(':')[1].strip()
	parts = card.split('|')
	winning_numbers_s = parts[0].strip()
	nums = ' ' + parts[1].strip() + ' '

	winning_numbers = winning_numbers_s.split(' ')

	for w_n in winning_numbers:
		w_n = w_n.strip()
		if len(w_n) == 0:
			continue
		if ' ' + w_n + ' ' in nums:
			card_score = card_score * 2 if card_score > 0 else 1
	score += card_score

print(score)