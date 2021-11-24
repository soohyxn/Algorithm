num = int(input())

def hanoi(n, p_from, p_to, p_mid):
	if n == 1:
		print(p_from, p_to)
		return

	hanoi(n-1, p_from, p_mid, p_to)
	print(p_from, p_to)
	hanoi(n-1, p_mid, p_to, p_from)

print((2**num)-1)
hanoi(num, 1, 3, 2)