from collections import deque

t = int(input())
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

def bfs():
    while queue:
        x, y = queue.popleft()
        flag = visited[x][y]

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < h and 0 <= ny < w:
                if visited[nx][ny] == -1 and board[nx][ny] == '.':
                    if flag == '*':
                        visited[nx][ny] = flag
                    else:
                        visited[nx][ny] = flag + 1
                    queue.append([nx, ny])
            else:
                if flag != '*':
                    return flag + 1

    return 'IMPOSSIBLE'

for _ in range(t):
    w, h = map(int, input().split())
    board, queue = [], deque()
    visited = [[-1] * w for _ in range(h)]

    for i in range(h):
        board.append(list(input()))

        for j in range(w):
            if board[i][j] == '@':
                start = [i, j]
                visited[i][j] = 0
            elif board[i][j] == '*':
                queue.append([i, j])
                visited[i][j] = '*'

    queue.append(start)
    print(bfs())