from collections import deque

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0] # 동남서북
queue = deque([])
answer = 0

# 모든 토마토 위치 큐에 넣기 (시작 위치들로부터 인접한 위치가 동시에 영향을 받음)
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append([i, j])

# dfs로 모든 토마토가 익을 최소 날짜 구하기
while queue:
    x, y = queue.popleft()

    # 4방향 탐색
    for i in range(4):
        xi = x + dx[i]
        yi = y + dy[i]

        # 상자의 범위를 벗어나면 넘어간다
        if xi < 0 or xi >= n or yi < 0 or yi >= m:
            continue

        # 아직 익지 않은 토마토라면 방문한다
        if graph[xi][yi] == 0:
            queue.append([xi, yi])
            graph[xi][yi] = graph[x][y] + 1

for i in range(n):
    for j in range(m):
        # 익지 않은 토마토가 있는 경우 모든 토마토가 익지 못하는 상황이므로 -1 리턴
        if graph[i][j] == 0:
            print(-1)
            exit(0)
        answer = max(answer, graph[i][j])

print(answer - 1)