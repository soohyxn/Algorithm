t = int(input())
nums = [int(input()) for _ in range(t)]
m = max(nums)
prime = [0, 0] + [1] * (m-1)

for i in range(2, int(m ** 0.5) + 1):
	if prime[i]:
		for j in range(i*2, m+1, i):
			prime[j] = 0
for num in nums:
	count = 0
	for i in range(2, num // 2 + 1):
		if prime[i] and prime[num - i]:
			count += 1
	print(count)