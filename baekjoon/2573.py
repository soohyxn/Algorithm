from collections import deque

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
ans = 1 # 빙산이 분리되는 시간

# 빙산 녹이기
def melt():
    height = [[0] * M for _ in range(N)] # 빙산의 녹은 높이

    # 빙산의 녹은 높이 구하기
    for x in range(N):
        for y in range(M):
            if board[x][y] > 0:
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 0:
                        height[x][y] -= 1

    # 녹은 높이만큼 빙산 높이 변경
    for x in range(N):
        for y in range(M):
            if board[x][y] + height[x][y] >= 0:
                board[x][y] += height[x][y]
            else: # 최저 높이는 0
                board[x][y] = 0

# 빙산 덩어리 구하기
def bfs(i, j):
    queue = deque([[i, j]])
    visited[i][j] = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and board[nx][ny] > 0:
                queue.append([nx, ny])
                visited[nx][ny] = 1

while True:
    melt() # 빙산 녹이기

    visited = [[0] * M for _ in range(N)]
    cnt = 0 # 빙산 덩어리 개수

    # 빙산 덩어리 구하기
    for x in range(N):
        for y in range(M):
            if not visited[x][y] and board[x][y] > 0:
                bfs(x, y)
                cnt += 1

    # 빙산이 다 녹을 때까지 분리되지 않는 경우
    if cnt == 0:
        print(0)
        exit(0)

    # 빙산의 덩어리가 2 이상인 경우 종료
    if cnt >= 2:
        break

    ans += 1

print(ans)