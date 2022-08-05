R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
ans = 1 # 지나갈 수 있는 최대 칸수

def bfs(i, j):
    global ans
    queue = set([(i, j, board[i][j])])

    while queue:
        x, y, visit = queue.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 이동 가능한 범위이며 지나온 알파벳인 아닌 경우 이동한다
            if 0 <= nx < R and 0 <= ny < C and board[nx][ny] not in visit:
                new_visit = visit + board[nx][ny]
                queue.add((nx, ny, new_visit))
                ans = max(ans, len(new_visit))

bfs(0, 0)
print(ans)