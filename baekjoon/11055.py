n = int(input())
nums = list(map(int, input().split()))
dp = [n for n in nums]

for i in range(1, n):
	for j in range(i):
		if nums[i] > nums[j]:
			dp[i] = max(dp[i], dp[j] + nums[i])
print(max(dp))