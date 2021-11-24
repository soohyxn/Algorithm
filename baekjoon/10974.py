from itertools import permutations

n = int(input())
nums = list(range(1, n+1))

for i in permutations(nums, n):
	print(*i)