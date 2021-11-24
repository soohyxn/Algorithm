from itertools import combinations_with_replacement

n, m = map(int, input().split())
nums = [i for i in range(1, n+1)] # 1부터 n까지 숫자 리스트
cr_nums = list(combinations_with_replacement(nums, m)) # 중복 조합 리스트

for num in cr_nums:
	for i in range(m):
		print(num[i], end = ' ')
	print()