from collections import deque
from itertools import combinations

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0] # 동남서북
virus, wall = [], 0 # 바이러스 위치 리스트, 벽의 개수
ans = [] # 바이러스를 퍼뜨리는 시간 리스트

for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            wall += 1
        elif board[i][j] == 2:
            virus.append([i, j])

def bfs(queue):
    time = 0 # 바이러스를 퍼뜨리는 시간
    # 바이러스 위치는 0초로
    for i, j in queue: 
        visited[i][j] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 이동 가능한 범위이며 벽이 아니고 아직 방문하지 않은 경우 바이러스가 퍼진다
            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] != 1 and visited[nx][ny] == -1:
                queue.append([nx, ny])
                visited[nx][ny] = visited[x][y] + 1
                # 빈칸인 경우만 시간 갱신
                if board[nx][ny] == 0:
                    time = max(time, visited[nx][ny])

    # 모든 빈칸에 바이러스가 퍼졌다면 시간 저장
    if list(sum(visited, [])).count(-1) == wall:
        ans.append(time)

for com in combinations(virus, M):
    queue = deque(list(com))
    visited = [[-1] * N for _ in range(N)]
    bfs(queue)

print(min(ans) if ans else -1)