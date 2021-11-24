from itertools import product

n, m = map(int, input().split())
nums = [i for i in range(1, n+1)] 
pr_nums = list(product(nums, repeat = m)) 

for num in pr_nums:
	for i in range(m):
		print(num[i], end = ' ')
	print()