import re

text_file = open("input-p1.txt", "r")
input = text_file.read()
text_file.close()

lines = input.splitlines()
hands = []
better_hands = []

rank = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
order = ['5k', '4k', 'fh', '3k', '2p', '1p', '0']


def calc_score(hand_s):
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

def goodify_hand(hand_s):
	exclude_list = []
	pair_cards = []
	triple_card = ''
	four_card = ''
	five_card = ''

	num_jokers = len(re.findall('J', hand_s))
	for char in hand_s:
		if char in exclude_list:
			continue
		exclude_list.append(char)

		matches = re.findall(char, hand_s)
		if len(matches) > 1:
			if len(matches) == 2:
				pair_cards.append(char)
			elif len(matches) == 3:
				triple_card = char
			elif len(matches) == 4:
				four_card = char
			elif len(matches) == 5:
				five_card = char

	if len(pair_cards) == 1 and triple_card != '':
		if num_jokers == 3:
			return hand_s.replace('J', pair_cards[0])
		return hand_s.replace('J', triple_card)
	elif len(pair_cards) == 2:
		if num_jokers == 2:
			j_k = pair_cards.index('J')
			return hand_s.replace('J', pair_cards[j_k - 1])
		if num_jokers == 1:
			p1 = rank.index(pair_cards[0])
			p2 = rank.index(pair_cards[1])
			if p1 < p2:
				return hand_s.replace('J', pair_cards[1])
			return hand_s.replace('J', pair_cards[0])
	elif four_card != '':
		if num_jokers == 1:
			return hand_s.replace('J', four_card)
		other_card = list(filter(lambda c: c != 'J', exclude_list))[0]
		return hand_s.replace('J', other_card)
	elif five_card != '':
		return hand_s
	elif triple_card != '':
		if num_jokers == 1:
			return hand_s.replace('J', triple_card)
		other_card = list(filter(lambda c: c != 'J', exclude_list))[0] # possibly upgrade
		return  hand_s.replace('J', other_card)
	elif len(pair_cards) == 1:
		if num_jokers == 1:
			return hand_s.replace('J', pair_cards[0])
		elif num_jokers == 2:
			other_card = list(filter(lambda c: c != 'J', exclude_list))[0] # possibly upgrade
			return hand_s.replace('J', other_card)
		return hand_s
	elif num_jokers == 1:
		other_card = list(filter(lambda c: c != 'J', exclude_list))[0] # possibly upgrade
		return hand_s.replace('J', other_card)

	return hand_s


for line in lines:
	parts = line.split()
	hand_string = parts[0]
	hands.append((hand_string, goodify_hand(hand_string)))

def sort_func(hand_tup):
	hand, better_hand = hand_tup
	score_s = calc_score(better_hand)

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
	hand, better_hand = rs[l]

	bid_search = re.search(rf'{hand} (\d+)', input)
	bid = bid_search.group(1)

	hand_rank = calc_score(hand)

	hand_score = inv_rank * int(bid)
	print(f'{hand} : {hand_rank}\t\t {bid} * {inv_rank} = {hand_score}')
	score += hand_score

print(score)




#251899709