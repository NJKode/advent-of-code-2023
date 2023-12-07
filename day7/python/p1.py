import re
from random import sample

text_file = open("input-p1-test.txt", "r")
input = text_file.read()
text_file.close()

all_lines = input.splitlines()
hands = []
bids = []
scores = []

rank = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
order = ['5k', '4k', 'fh', '3k', '2p', '1p', '0']
order

# lines = sample(all_lines, 10)
lines = all_lines

for line in lines:
	parts = line.split()
	hands.append(parts[0])

def find_stuff(hand_s):
	exclude_list = []
	pair_count = 0
	has_triple = False,
	has_four = False,
	has_five = False
	highest_card = '2'
	for char in hand_s:
		if char in exclude_list:
			continue
		exclude_list.append(char)

		if rank.index(char) < rank.index(highest_card):
			highest_card = char

		matches = re.findall(char, hand_s)
		if len(matches) > 1:
			if len(matches) == 2:
				pair_count += 1
			elif len(matches) == 3:
				has_triple = True
			elif len(matches) == 4:
				has_four = True
			elif len(matches) == 5:
				has_five = True

	if pair_count == 1 and has_triple == True:
		return 'fh'
	elif pair_count == 2:
		return '2p'
	elif has_four == True:
		return '4k'
	elif has_five == True:
		return '5k'
	elif has_triple == True:
		return '3k'
	elif pair_count == 1:
		return '1p'

	return '0'


def sort_func(hand):
	score_s = find_stuff(hand)

	mod = len(rank)

	score_1 = (mod - rank.index(hand[0])) * mod * 10000000000000
	score_2 = (mod - rank.index(hand[1])) * mod * 1000000000
	score_3 = (mod - rank.index(hand[2])) * mod * 1000000
	score_4 = (mod - rank.index(hand[3])) * mod * 1000
	score_5 = (mod - rank.index(hand[4])) * mod

	main_score = (len(order) - order.index(score_s)) * len(order) * 10000000000000000

	score_index = (main_score + score_1 + score_2 + score_3 + score_4 + score_5)
	# print(f'{hand}: {main_score} + {score_1} + {score_2} + {score_3} + {score_4} + {score_5} = {score_index}')
	return score_index

rs = sorted(hands, key=sort_func)

score = 0
for l in range(len(rs)):
	inv_rank = l + 1
	hand = rs[l]

	bid_search = re.search(rf'{hand} (\d+)', input)
	bid = bid_search.group(1)

	hand_rank = find_stuff(hand)

	hand_score = inv_rank * int(bid)
	print(f'{hand} : {hand_rank}\t\t {bid} * {inv_rank} = {hand_score}')
	score += hand_score

print(score)




#251899709