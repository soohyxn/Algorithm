import sys
sys.setrecursionlimit(10**7)

M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(M)]
dp =[[-1] * N for _ in range(M)]
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1] # 북동남서

def dfs(x, y):
    if x == M-1 and y == N-1: # 도착한 경우
        return 1
    
    if dp[x][y] != -1: # 방문했던 위치인 경우 경로값 리턴
        return dp[x][y]
    
    dp[x][y] = 0 # 방문하지 않은 경우 방문처리

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < M and 0 <= ny < N and graph[nx][ny] < graph[x][y]: # 이동 가능한 범위에 있으며 내리막길인 경우 경로탐색
            dp[x][y] += dfs(nx, ny)

    return dp[x][y]

print(dfs(0, 0))