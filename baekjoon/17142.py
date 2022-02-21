from collections import deque
from itertools import combinations

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0] # 동남서북
virus, ans =  [], [] # 바이러스 위치 리스트, 바이러스를 퍼뜨리는 시간 리스트
cnt_wall = 0 # 벽의 개수

# 바이러스 위치와 벽의 개수 구하기
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            cnt_wall += 1
        elif graph[i][j] == 2:
            virus.append([i, j])

def bfs(queue):
    time = 0 # 바이러스를 퍼뜨리는 시간
    for i, j in queue:
        visited[i][j] = 0 # 바이러스 위치는 0초로

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 이동 가능한 범위이며 벽이 아니고 아직 방문하지 않은 경우 바이러스를 퍼뜨린다
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] != 1 and visited[nx][ny] == -1:
                queue.append([nx, ny])
                visited[nx][ny] = visited[x][y] + 1
                if graph[nx][ny] == 0: # 빈칸인 경우 시간 갱신
                    time = max(time, visited[nx][ny])

    # 방문하지 않는 곳의 개수가 벽의 개수와 동일하다면 모든 빈칸에 바이러스가 퍼진 것이므로 시간을 저장
    if list(sum(visited, [])).count(-1) == cnt_wall:
        ans.append(time)

for com in combinations(virus, m):
    queue = deque(list(com))
    visited = [[-1] * n for _ in range(n)]
    bfs(queue)

print(min(ans) if ans else -1)