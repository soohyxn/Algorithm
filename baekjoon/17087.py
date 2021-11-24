n, S = map(int, input().split())
pos = list(map(int, input().split()))
dif = list(set(abs(p - S) for p in pos))
D = min(dif)

def gcd(a, b):
	res = 0
	while b:
		res = a % b
		a = b
		b = res
	return a

for d in dif:
	D = gcd(d, D)
print(D)