from collections import deque

N, M = map(int, input().split())
graph = [list(input()) for _ in range(M)]
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
answer = [0, 0]

def bfs(i, j):
    global answer
    queue = deque([[i, j]])
    status = graph[i][j]
    graph[i][j] = 0
    cnt = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            if graph[nx][ny] == status:
                queue.append([nx, ny])
                graph[nx][ny] = 0
                cnt += 1
              
    if status == 'W':
        answer[0] += cnt ** 2
    else:
        answer[1] += cnt ** 2

for i in range(M):
    for j in range(N):
        if graph[i][j] != 0:
            bfs(i, j)
print(*answer)