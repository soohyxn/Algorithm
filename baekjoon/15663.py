from itertools import permutations

n, m = map(int, input().split())
nums = list(map(int, input().split()))

cb = permutations(nums, m)
cb = list(set(cb))
cb.sort()
for i in cb:
	print(*i)