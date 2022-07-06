from collections import deque

M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0] # 동남서북
queue = deque()
ans = 0

# 토마토 위치 큐에 삽입
for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            queue.append([i, j])

# 인접한 토마토 익기
def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 0: # 범위 내에 있으며 안 익은 토마토인 경우
                queue.append([nx, ny])
                board[nx][ny] = board[x][y] + 1

bfs()
# 토마토가 모두 익을 최소 날짜 구하기
for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            print(-1)
            exit(0)
        ans = max(ans, board[i][j])

print(ans - 1)