N, K = map(int, input().split())
thing = [list(map(int, input().split())) for _ in range(N)]
dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, K+1):
        w, v = thing[i-1]
        if j < w: # 현재물건의 무게가 탐색하는 무게보다 작다면 이전값을 그대로 가져온다
            dp[i][j] = dp[i-1][j]
        else: # 크다면 이전값과 현재 물건을 넣어 다른 물건들로 채운 값을 비교하여 큰 값을 저정한다
            dp[i][j] = max(dp[i-1][j], v + dp[i-1][j-w])

print(dp[N][K])