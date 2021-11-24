n = int(input())
answer = 0

for i in range(1, n+1):
	result = sum(list(map(int, str(i))))
	if i + result == n:
		print(i)
		break

	if i == n:
		print(0)