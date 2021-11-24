from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(i, j):
    queue = deque([[i, j]])

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            xi = x + dx[i]
            yi = y + dy[i]
            if xi <= -1 or xi >= n or yi <= -1 or yi >= m:
                continue
            if graph[xi][yi] == 1:
                queue.append([xi, yi])
                graph[xi][yi] = graph[x][y] + 1

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            bfs(i, j)

print(graph[n-1][m-1])