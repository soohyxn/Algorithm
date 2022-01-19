def solution(land):
    n, m = len(land), len(land[0])
    dp = [[0] * m for _ in range(n)]
    
    for i in range(n): # 현재 탐색하는 땅의 행
        for j in range(m): # 현재 탐색하는 땅의 열
            for k in range(m): # 현재 탐색하는 땅의 이전 열
                if j != k: # 같은 열이 아닌 경우 최대값 구하기
                    dp[i][j] = max(dp[i][j], land[i][j] + dp[i-1][k])

    return max(dp[-1])