from itertools import permutations

n, m = map(int, input().split())
nums = [i for i in range(1, n+1)]
pm_nums = list(permutations(nums, m))

for num in pm_nums:
	for i in range(m):
		print(num[i], end = ' ')
	print()