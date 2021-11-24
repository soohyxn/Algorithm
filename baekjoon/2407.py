n, m = map(int, input().split())
answer = 1
k = n - m

while n > k:
	answer *= n
	n -= 1
while m > 1:
	answer //= m
	m -= 1
print(answer)