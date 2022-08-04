from collections import deque

N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

queue = []
for i in range(N):
    for j in range(N):
        if board[i][j] != 0:
            queue.append([board[i][j], i, j, 0]) # 바이러스 종류, x위치, y위치, 시간
queue.sort() # 바이러스 종류 오름차순 정렬
queue = deque(queue)

def bfs():
    while queue:
        num, x, y, time = queue.popleft()
        # S초가 되면 종료
        if time == S:
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 이동 가능한 범위이며 빈칸인 경우 바이러스가 퍼진다
            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == 0:
                queue.append([num, nx, ny, time+1])
                board[nx][ny] = num

bfs()
print(board[X-1][Y-1])