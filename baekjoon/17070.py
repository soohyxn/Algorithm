n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[[0] * n for _ in range(n)] for _ in range(3)] # 0: 가로, 1: 세로, 2: 대각선
dp[0][0][1] = 1 # 처음 위치 초기화

# 0번째 행 초기화
for j in range(2, n):
    if board[0][j] == 0:
        dp[0][0][j] = dp[0][0][j-1]

for i in range(1, n):
    for j in range(1, n):
        # 대각선인 경우
        if board[i][j] == 0 and board[i-1][j] == 0 and board[i][j-1] == 0:
            dp[2][i][j] = dp[0][i-1][j-1] + dp[1][i-1][j-1] + dp[2][i-1][j-1]
        # 가로, 세로인 경우
        if board[i][j] == 0:
            dp[0][i][j] = dp[0][i][j-1] + dp[2][i][j-1] # 가로
            dp[1][i][j] = dp[1][i-1][j] + dp[2][i-1][j] # 세로

print(sum([dp[i][n-1][n-1] for i in range(3)]))