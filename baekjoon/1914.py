n = int(input())
def hanoi(n, p_from, p_mid, p_to):
	if n == 1:
		print(p_from, p_to)
		return

	hanoi(n-1, p_from, p_to, p_mid)
	print(p_from, p_to)
	hanoi(n-1, p_mid, p_from, p_to)

print(2 ** n - 1)
if n <= 20: hanoi(n, 1, 2, 3)	