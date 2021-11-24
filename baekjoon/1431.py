n = int(input())
serial = [input() for _ in range(n)]

def s_num(x):
	result = [int(n) for n in x if n.isdigit()]
	return sum(result)

serial.sort(key=lambda x : (len(x), s_num(x), x))

for s in serial:
	print(s)