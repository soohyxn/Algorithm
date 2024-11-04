n, k = map(int, input().split())
dp = [[1] * (n+1) for _ in range(k+1)] # k개 합이 n이 되는 경우의 수

for i in range(2, k+1):
    for j in range(1, n+1):
        dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000000

print(dp[k][n])