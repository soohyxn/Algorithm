N, K = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * (K+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, K+1):
        W, V = items[i-1] # 탐색하는 물건
        if j < W: # 헤딩 무게가 탐색하는 물건의 무게보다 작다면 담을 수 없으므로 이전값을 그대로 가져온다
            dp[i][j] = dp[i-1][j]
        else: # 크다면 이전값과 현재 물건을 넣고 다른 물건들로 채운 값을 비교하여 큰 값을 저장한다
            dp[i][j] = max(dp[i-1][j], V + dp[i-1][j-W])

print(dp[N][K]) # 배낭에 넣을 수 있는 최대 가치합