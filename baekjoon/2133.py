N = int(input())
dp = [0] * 31 # N+1 크기로 생성하면 IndexError가 난다
dp[2] = 3

for i in range(4, N+1, 2):
    # dp[i-2] * 3 = 길이가 n-2인 타일 경우에 길이가 2인 타일(3가지) 븥인 경우
    # sum(dp[:i-2]) * 2 = 길이가 0부터 n-4까지인 타일 경우에 나눌 수 없는 자신(2가지)을 붙인 경우
    # 2 = 길이가 n인 타일을 새로 만드는 경우
    dp[i] = dp[i-2] * 3 + sum(dp[:i-2]) * 2 + 2

print(dp[N])