n = int(input())
nums = list(map(int, input().split()))
dp = [[0] * 21 for _ in range(n)]
dp[0][nums[0]] = 1

for i in range(1, n-1):
    for j in range(21):
        if dp[i-1][j]:
            # 현재 숫자를 더하는 경우
            if 0 <= j + nums[i] <= 20:
                dp[i][j + nums[i]] += dp[i-1][j]
            # 현재 숫자를 빼는 경우
            if 0 <= j - nums[i] <= 20:
                dp[i][j - nums[i]] += dp[i-1][j]

print(dp[n-2][nums[-1]])