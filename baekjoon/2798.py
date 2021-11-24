n, m = map(int, input().split())
cards = list(map(int, input().split()))
answer = 0

for i in range(n):
	for j in range(i+1, n):
		for k in range(j+1, n):
			result = cards[i] + cards[j] + cards[k]
			if result <= m:
				answer = max(answer, result)

print(answer)