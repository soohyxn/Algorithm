from collections import deque

n = int(input())
graph = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
min_h, max_h = 1e9, 0
answer = 0

for _ in range(n):
    s = list(map(int, input().split()))
    min_h = min(min_h, min(s))
    max_h = max(max_h, max(s))
    graph.append(s)

def bfs(i, j, h, visited):
    queue = deque([[i, j]])
    visited[i][j] = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            xi = x + dx[i]
            yi = y + dy[i]
            if xi < 0 or xi >= n or yi < 0 or yi >= n:
                continue
            if not visited[xi][yi] and graph[xi][yi] >= h:
                queue.append([xi, yi])
                visited[xi][yi] = 1

for h in range(min_h, max_h+1):
    count = 0
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and graph[i][j] >= h:
                bfs(i, j, h, visited)
                count += 1
    answer = max(answer, count)
print(answer)