from collections import deque

M, N, K = map(int, input().split())
graph = [[0] * M for _ in range(N)]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0] # 동서남북
answer = [] # 각 영역의 넓이

# 직사각형에 해당하는 영역을 1로 만들어준다
for _ in range(K):
    left_x, left_y, right_x, right_y = map(int, input().split())
    
    for i in range(left_x, right_x):
        for j in range(left_y, right_y):
            graph[i][j] = 1

def bfs(i, j):
    queue = deque([[i, j]])
    graph[i][j] = 1
    count = 1 # 영역의 넓이

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0: # 범위 안에 있고 아직 방문하지 않았다면 방문처리
                queue.append([nx, ny])
                graph[nx][ny] = 1
                count += 1
    return count

# 분리된 영역 구하기
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            result = bfs(i, j)
            answer.append(result)

answer.sort()
print(len(answer))
print(*answer)