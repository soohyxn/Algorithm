n = int(input())
cards = {}
for _ in range(n):
	c = int(input())
	if c in cards: cards[c] += 1
	else: cards[c] = 1
	
cards = sorted(cards.items(), key=lambda x: (-x[1], x[0]))
print(cards[0][0])