from collections import deque

T = int(input())
dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

def bfs(i, j):
    queue = deque([[i, j]])
    graph[i][j] = 1

    while queue:
        x, y = queue.popleft()
        if x == move_x and y == move_y:
            return graph[x][y] - 1
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < l and 0 <= ny < l:
                if graph[nx][ny] == 0:
                    queue.append([nx, ny])
                    graph[nx][ny] = graph[x][y] + 1

for _ in range(T):
    l = int(input())
    graph = [[0] * l for _ in range(l)]
    now_x, now_y = map(int, input().split())
    move_x, move_y = map(int, input().split())

    if now_x == move_x and now_y == move_y:
        print(0)
    else:
        result = bfs(now_x, now_y)
        print(result)