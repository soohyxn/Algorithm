from itertools import combinations

n, m = map(int, input().split())
nums = [i for i in range(1, n+1)] # 1부터 n까지 숫자 리스트
pm_nums = list(combinations(nums, m)) # 조합 리스트

for num in pm_nums:
	for i in range(m):
		print(num[i], end = ' ')
	print()