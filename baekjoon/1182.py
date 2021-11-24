from itertools import combinations

n, S = map(int, input().split())
nums = list(map(int, input().split()))
count = 0

for i in range(1, n+1):
	for cb in list(combinations(nums, i)):
		if sum(cb) == S:
			count += 1
print(count)