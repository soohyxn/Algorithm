n = int(input())
prime = [0, 0] + [1] * 9999

for i in range(2, int(10000 ** 0.5)+1):
	if prime[i]:
		for j in range(i*2, 10001, i):
			prime[j] = 0

for _ in range(n):
	num = int(input())
	idx = 0
	while True:
		if prime[num // 2 - idx] and prime[num // 2 + idx]:
			print(num // 2 - idx, num // 2 + idx)
			break
		idx += 1