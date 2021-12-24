n = int(input())
nums = list(map(int, input().split()))
reverse_nums = nums[::-1]
increase = [1] * n
decrease = [1] * n
dp = [0] * n

for i in range(1, n):
    for j in range(i):
        if nums[i] > nums[j]:
            increase[i] = max(increase[i], increase[j] + 1)
        if reverse_nums[i] > reverse_nums[j]:
            decrease[i] = max(decrease[i], decrease[j] + 1)

for i in range(n):
    dp[i] = increase[i] + decrease[n-i-1] - 1
print(max(dp))