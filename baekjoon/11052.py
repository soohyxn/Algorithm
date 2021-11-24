n = int(input())
cards = [0] + list(map(int, input().split()))
dp = [c for c in cards]

for i in range(2, n+1):
    for j in range(1, i//2+1):
        dp[i] = max(dp[i], dp[j] + dp[i-j])

print(dp[n])