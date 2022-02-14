from collections import deque

n, m = map(int, input().split())
map = [list(input()) for _ in range(n)]
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1] # 북동남서
ans = 0 # 최대 최단거리

def bfs(i, j):
    queue = deque([[i, j]])
    visited = [[0] * m for _ in range(n)]
    visited[i][j] = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and map[nx][ny] == 'L': # 이동 가능한 범위이며 아직 방문하지 않았고 육지인 경우
                queue.append([nx, ny])
                visited[nx][ny] = visited[x][y] + 1

    return max([max(v) for v in visited]) - 1

for i in range(n):
    for j in range(m):
        if map[i][j] == 'L': # 모든 육지에서 최단거리를 구한다
            dist = bfs(i, j)
            ans = max(ans, dist)

print(ans)