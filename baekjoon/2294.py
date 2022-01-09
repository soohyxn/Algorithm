n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]
dp = [0] + [1e9] * k

for c in coin:
    for i in range(c, k+1):
        dp[i] = min(dp[i], dp[i-c]+1)

if dp[k] == 1e9:
    print(-1)
else:
    print(dp[k])