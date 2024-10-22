n = int(input())
cards = list(map(int, input().split()))
dp = cards[:] # 카드비용의 최대값 리스트

for i in range(n):
    for j in range(i):
        dp[i] = max(dp[i], dp[j] + dp[i-j-1])

print(dp[n-1])