s = int(input())
i, n = 1, 0

while True:
	s -= i

	if s >= 0:
		n += 1
		i += 1
	else:
		print(n)
		break