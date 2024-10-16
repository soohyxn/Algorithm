from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input())) for _ in range(n)]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0] # 동남서북

def bfs(a, b):
    queue = deque([[a, b]])

    while queue:
        x, y = queue.popleft()

        # 4방향 탐색
        for i in range(4):
            xi = x + dx[i]
            yi = y + dy[i]

            # 미로의 범위를 벗어나면 넘어간다
            if xi < 0 or xi >= n or yi < 0 or yi >= m:
                continue
            
            # 이동할 수 있으면 이동 칸수 계산
            if board[xi][yi] == 1:
                queue.append([xi, yi])
                board[xi][yi] = board[x][y] + 1

bfs(0, 0)
print(board[n-1][m-1])