from collections import deque

N, K = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
queue = []

for i in range(N):
    for j in range(N):
        if graph[i][j] != 0:
            queue.append([graph[i][j], i, j, 0]) # 바이러스 종류, x위치, y위치, 시간

queue.sort() # 오름차순 정렬
queue = deque(queue)

def bfs():
    while queue:
        virus, x, y, time = queue.popleft()
        if time == S: # S초가 되면 멈춤
            break
        # 상, 하, 좌, 우 확인
        for i in range(4):
            xi = x + dx[i]
            yi = y + dy[i]
            if 0 <= xi < N and 0 <= yi < N and graph[xi][yi] == 0: # 범위 안에 있고 바이러스가 들어가지 않은 상태라면
                graph[xi][yi] = virus
                queue.append([virus, xi, yi, time + 1])

bfs()
print(graph[X-1][Y-1])