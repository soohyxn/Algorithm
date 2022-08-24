T, W = map(int, input().split())
tree = [int(input()) for _ in range(T)]
dp = [[0] * (W+1) for _ in range(T)]

for i in range(T):
    for j in range(W+1):
        # 움직이지 않은 경우
        if j == 0:
            # 1번 나무라면 열매를 받을 수 있다
            if tree[i] == 1:
                dp[i][0] = dp[i-1][0] + 1
            # 2번 나무라면 열매를 받을 수 업다
            else:
                dp[i][0] = dp[i-1][0]
        # 움직인 경우
        else:
            # 1번 나무이며 이동횟수가 짝수인 경우 열매를 받을 수 있다
            if tree[i] == 1 and j % 2 == 0:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + 1
            # 2번 나무이며 이동횟수가 홀수인 경우 열매를 받을 수 있다
            elif tree[i] == 2 and j % 2 == 1:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + 1
            # 그렇지 않은 경우 열매를 받을 수 없다
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1])

print(max(dp[-1]))