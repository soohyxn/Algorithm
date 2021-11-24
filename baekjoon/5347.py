n = int(input())

def gcd(a, b):
	res = 0
	while b:
		res = a % b
		a = b
		b = res
	return a

def lcm(a, b):
	return (a * b) // gcd(a, b)

for _ in range(n):
	a, b = map(int, input().split())
	print(lcm(a, b))