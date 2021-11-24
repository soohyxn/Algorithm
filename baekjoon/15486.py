import sys

n = int(sys.stdin.readline())
t, p = [], []
dp = [0] * (n + 1)

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    t.append(a)
    p.append(b)

K = 0
for i in range(n):
    K = max(K, dp[i])
    if i + t[i] > n:
        continue
    dp[i + t[i]] = max(dp[i + t[i]], K + p[i])

print(max(dp))