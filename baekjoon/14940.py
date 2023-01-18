from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dist = [[-1] * m for _ in range(n)]
visited = [[0] * m for _ in range(n)]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0] # 동남서북

def bfs(i, j):
    queue = deque([[i, j]])
    dist[i][j] = 0
    visited[i][j] = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 이동 가능한 범위에 있으며 갈 수 있는 땅이고 아직 방문하지 않은 경우
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 1 and not visited[nx][ny]:
                dist[nx][ny] = dist[x][y] + 1
                visited[nx][ny] = 1
                queue.append([nx, ny])

for i in range(n):
    for j in range(m):
        if board[i][j] == 0: # 갈 수 없는 땅은 0
            dist[i][j] = 0
        elif board[i][j] == 2: # 목표지점이면 거리를 구한다
            bfs(i, j)

for d in dist:
    print(*d)