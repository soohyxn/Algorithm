T = int(input())

dp = [1] * 10001 # 숫자 1만 사용하는 경우로 초기화
# 숫자 2 사용
for i in range(2, 10001):
    dp[i] += dp[i-2]

# 숫자 3 사용
for i in range(3, 10001):
    dp[i] += dp[i-3]

for _ in range(T):
    n = int(input())
    print(dp[n])