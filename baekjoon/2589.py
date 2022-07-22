from collections import deque

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0] # 동남서북
ans = 0 # 최대 최단거리

# 보물이 묻혀 있는 두 곳 간의 최단 거리 구하기
def bfs(i, j):
    queue = deque([[i, j]])
    visited = [[0] * M for _ in range(N)] # 각 위치의 최단거리
    visited[i][j] = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 이동 가능한 범위이며 아직 방문하지 않았고 육지인 경우 다음 위치로 이동한다
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and board[nx][ny] == 'L':
                queue.append([nx, ny])
                visited[nx][ny] = visited[x][y] + 1

    return max([max(v) for v in visited]) - 1 # 최단거리

# 모든 육지의 최단거리 구하기
for i in range(N):
    for j in range(M):
        # 해당 위치가 육지라면 보물을 묻을 수 있으므로 최단거리를 구한다
        if board[i][j] == 'L':
            result = bfs(i, j)
            ans = max(ans, result)

print(ans)