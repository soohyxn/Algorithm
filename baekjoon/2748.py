n = int(input())
a, b, result = 0, 1, 1
for _ in range(2, n+1):
	result = a + b
	a = b
	b = result
print(result)