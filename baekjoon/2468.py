from collections import deque

n = int(input())
graph = []
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0] # 동남서북
max_h = 0 # 지역의 최대 높이
answer = 0

for _ in range(n):
    g = list(map(int, input().split()))
    graph.append(g)
    max_h = max(max_h, max(g))

def dfs(a, b, height, visited):
    queue = deque([[a, b]])
    visited[a][b] = 1

    while queue:
        x, y = queue.popleft()

        # 4방향 탐색
        for i in range(4):
            xi = x + dx[i]
            yi = y + dy[i]

            # 지역 범위를 벗어나면 넘어간다
            if xi < 0 or xi >= n or yi < 0 or yi >= n:
                continue

            # 아직 방문하지 않고 물에 잠기지 않는 경우 탐색한다
            if not visited[xi][yi] and graph[xi][yi] > height:
                queue.append([xi, yi])
                visited[xi][yi] = 1

# 비의 양에 따른 모든 경우 탐색
for h in range(max_h + 1):
    count = 0 # 안전한 영역의 개수
    visited = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and graph[i][j] > h:
                dfs(i, j, h, visited)
                count += 1

    answer = max(answer, count)

print(answer)