num = list(map(int, input()))
n = len(num)
dp = [0] * (n+1)

if num[0] == 0:
    print(0)
else:
    num = [0] + num
    dp[0] = dp[1] = 1

    for i in range(2, n+1):
        if num[i] > 0:
            dp[i] = dp[i-1]

        k = num[i-1] * 10 + num[i]
        if 10 <= k <= 26:
            dp[i] += dp[i-2]

    print(dp[n] % 1000000)